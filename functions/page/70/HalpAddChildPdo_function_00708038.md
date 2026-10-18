# HalpAddChildPdo

- RVA: `0x00708038`–`0x00708054` (길이 `28` bytes)
- VA: `0x0000000140708038`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `10`개 명령, `28/28` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [HalpAddDevice](HalpAddDevice_function_00708060.md) at `0x0070818C`
- [HalpAddDevice](HalpAddDevice_function_00708060.md) at `0x007081F2`
- [HalpAddDevice](HalpAddDevice_function_00708060.md) at `0x007082A3`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00708038  48 83 7A 08 00                  cmp qword ptr [rdx + 8], 0
0070803D  75 04                           jne 0x140708043
0070803F  48 89 4A 08                     mov qword ptr [rdx + 8], rcx
00708043  49 8B 00                        mov rax, qword ptr [r8]
00708046  48 85 C0                        test rax, rax
00708049  74 04                           je 0x14070804f
0070804B  48 89 48 08                     mov qword ptr [rax + 8], rcx
0070804F  49 89 08                        mov qword ptr [r8], rcx
00708052  C3                              ret
00708053  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpAddChildPdo(__int64 a1, __int64 a2, __int64 a3)
{
    if ((*(unsigned __int64 *)(a2 + 8)) == 0) {
        *(unsigned __int64 *)(a2 + 8) = a1;
    }
    if (*(unsigned __int64 *)(a3) != 0) {
        *(unsigned __int64 *)(*(unsigned __int64 *)(a3) + 8) = a1;
    }
    *(unsigned __int64 *)(a3) = a1;
    return *(unsigned __int64 *)(a3);
}
```

## 5. (Beta) C Style

```c
int64_t HalpAddChildPdo(int64_t Arg1, void *Arg2, void *Arg3)
{
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg3 = (uint8_t *)Arg3;

    if ((*(uint64_t *)(arg2 + 0x8)) == 0) {
        *(uint64_t *)(arg2 + 0x8) = Arg1;
    }
    if (*(uint64_t *)(arg3) != 0) {
        *(uint64_t *)(*(uint64_t *)(arg3) + 0x8) = Arg1;
    }
    *(uint64_t *)(arg3) = Arg1;
    return *(uint64_t *)(arg3);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x8` | `64` | `R` |
| `Arg2` | `+ 0x8` | `64` | `W` |
| `Arg3` | `+ 0x0` | `64` | `R` |
| `Arg3` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00708038&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00708038[BB_00708038]
  bb_0070803F[BB_0070803F]
  bb_00708043[BB_00708043]
  bb_0070804B[BB_0070804B]
  bb_0070804F[BB_0070804F]
  bb_00708053[BB_00708053]
  bb_00708038 -->|branch| bb_00708043
  bb_00708038 -->|fallthrough| bb_0070803F
  bb_0070803F -->|flow| bb_00708043
  bb_00708043 -->|branch| bb_0070804F
  bb_00708043 -->|fallthrough| bb_0070804B
  bb_0070804B -->|flow| bb_0070804F
```
