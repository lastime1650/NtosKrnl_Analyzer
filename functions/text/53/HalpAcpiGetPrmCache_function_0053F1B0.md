# HalpAcpiGetPrmCache

- RVA: `0x0053F1B0`–`0x0053F1C6` (길이 `22` bytes)
- VA: `0x000000014053F1B0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `6`개 명령, `22/22` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0053F1B0` → RVA `0x00E0F650` (`.data`; read)
- `0x0053F1BA` → RVA `0x00E0F688` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0053F1B0  48 8D 05 99 04 8D 00            lea rax, [rip + 0x8d0499]
0053F1B7  48 89 02                        mov qword ptr [rdx], rax
0053F1BA  48 8D 05 C7 04 8D 00            lea rax, [rip + 0x8d04c7]
0053F1C1  48 89 01                        mov qword ptr [rcx], rax
0053F1C4  C3                              ret
0053F1C5  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpAcpiGetPrmCache(__int64 a1, __int64 a2)
{
    *(unsigned __int64 *)(a2) = v_rip + 9241753;
    *(unsigned __int64 *)(a1) = v_rip + 9241799;
    return v_rip + 9241799;
}
```

## 5. (Beta) C Style

```c
int64_t HalpAcpiGetPrmCache(void *Arg1, void *Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    *(uint64_t *)(arg2) = v_rip + 9241753;
    *(uint64_t *)(arg1) = v_rip + 9241799;
    return v_rip + 9241799;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `W` |
| `Arg2` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0053F1B0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0053F1B0[BB_0053F1B0]
  bb_0053F1C5[BB_0053F1C5]
```
