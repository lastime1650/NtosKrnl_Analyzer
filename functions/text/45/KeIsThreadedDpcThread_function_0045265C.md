# KeIsThreadedDpcThread

- RVA: `0x0045265C`–`0x00452672` (길이 `22` bytes)
- VA: `0x000000014045265C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `6`개 명령, `22/22` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [MiGroupZeroHugeRange](../68/MiGroupZeroHugeRange_function_0068C384.md) at `0x0068C3F6`

### Static image references
- `0x00452663` → RVA `0x005C84F0` (`KiExecuteDpc`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0045265C  48 8B 81 60 05 00 00            mov rax, qword ptr [rcx + 0x560]
00452663  48 8D 0D 86 5E 17 00            lea rcx, [rip + 0x175e86]
0045266A  48 3B C1                        cmp rax, rcx
0045266D  0F 94 C0                        sete al
00452670  C3                              ret
00452671  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KeIsThreadedDpcThread(__int64 a1)
{
    __int64 result;

    result = ((*(unsigned __int64 *)(a1 + 1376)) == (v_rip + 1531526)) ? 1 : 0;
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t KeIsThreadedDpcThread(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;

    result = ((*(uint64_t *)(arg1 + 0x560)) == (v_rip + 1531526)) ? 1 : 0;
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x560` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0045265C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0045265C[BB_0045265C]
  bb_00452671[BB_00452671]
```
