# MiGetNodeSystemInformation

- RVA: `0x0047D390`–`0x0047D3AB` (길이 `27` bytes)
- VA: `0x000000014047D390`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `7`개 명령, `27/27` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [MiCreatePerNodeZeroingConductor](../../page/81/MiCreatePerNodeZeroingConductor_function_00810480.md) at `0x008104BA`

### Static image references
- `0x0047D396` → RVA `0x00E2DBF8` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0047D390  8B C1                           mov eax, ecx
0047D392  48 8D 0C 40                     lea rcx, [rax + rax*2]
0047D396  48 8B 05 5B 08 9B 00            mov rax, qword ptr [rip + 0x9b085b]
0047D39D  48 C1 E1 07                     shl rcx, 7
0047D3A1  48 8B 84 01 78 01 00 00         mov rax, qword ptr [rcx + rax + 0x178]
0047D3A9  C3                              ret
0047D3AA  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiGetNodeSystemInformation(int a1)
{
    a1 = ((unsigned int)(a1) + (unsigned int)(a1) * 2) << (7);
    return *(unsigned __int64 *)(a1 + *(unsigned __int64 *)(v_rip + 10160219) * 1 + 376);
}
```

## 5. (Beta) C Style

```c
int64_t MiGetNodeSystemInformation(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    Arg1 = ((uint32_t)(Arg1) + (uint32_t)(Arg1) * 2) << (7);
    return *(uint64_t *)(arg1 + *(uint64_t *)(v_rip + 0x9B085B) * 1 + 0x178);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0 + rax*2` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0047D390&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0047D390[BB_0047D390]
  bb_0047D3AA[BB_0047D3AA]
```
