# I_MinCryptGetSigningTime$fin$0

- RVA: `0x00B15D50`–`0x00B15D8A` (길이 `58` bytes)
- VA: `0x0000000140B15D50`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000C5CF8`
- 디코드: `19`개 명령, `58/58` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00B15D72` → [I_MinCryptBuildErrorPolicy](../83/I_MinCryptBuildErrorPolicy_function_008391DC.md) (function, `0x008391DC`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00B15D50  40 55                           push rbp
00B15D52  48 83 EC 50                     sub rsp, 0x50
00B15D56  48 8B EA                        mov rbp, rdx
00B15D59  0F B6 C1                        movzx eax, cl
00B15D5C  84 C9                           test cl, cl
00B15D5E  75 1C                           jne 0x140b15d7c
00B15D60  8B 4D 50                        mov ecx, dword ptr [rbp + 0x50]
00B15D63  85 C9                           test ecx, ecx
00B15D65  79 1C                           jns 0x140b15d83
00B15D67  44 8B 45 54                     mov r8d, dword ptr [rbp + 0x54]
00B15D6B  48 8B 95 B8 00 00 00            mov rdx, qword ptr [rbp + 0xb8]
00B15D72  E8 65 34 D2 FF                  call 0x1408391dc
00B15D77  89 45 50                        mov dword ptr [rbp + 0x50], eax
00B15D7A  EB 07                           jmp 0x140b15d83
00B15D7C  C7 45 50 E8 00 00 C0            mov dword ptr [rbp + 0x50], 0xc00000e8
00B15D83  48 83 C4 50                     add rsp, 0x50
00B15D87  5D                              pop rbp
00B15D88  C3                              ret
00B15D89  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall I_MinCryptGetSigningTime_fin_0(unsigned __int8 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (80);
    if (a1 != 0) goto loc_00B15D7C;
    if (!sign_flag) goto loc_00B15D83;
    result = I_MinCryptBuildErrorPolicy((unsigned int)(*(unsigned int *)(a2 + 80)), *(unsigned __int64 *)(a2 + 184), (unsigned int)(*(unsigned int *)(a2 + 84)), a4);
    *(unsigned int *)(a2 + 80) = (unsigned int)(result);
    goto loc_00B15D83;
loc_00B15D7C:
    *(unsigned int *)(a2 + 80) = 0xC00000E8ULL;
loc_00B15D83:
    v_rsp = (v_rsp) + (80);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t I_MinCryptGetSigningTime_fin_0(uint8_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (80);
    if (Arg1 != 0) goto loc_00B15D7C;
    if (!sign_flag) goto loc_00B15D83;
    result = I_MinCryptBuildErrorPolicy((uint32_t)(*(uint32_t *)(arg2 + 0x50)), *(uint64_t *)(arg2 + 0xB8), (uint32_t)(*(uint32_t *)(arg2 + 0x54)), a4);
    *(uint32_t *)(arg2 + 0x50) = (uint32_t)(result);
    goto loc_00B15D83;
loc_00B15D7C:
    *(uint32_t *)(arg2 + 0x50) = 0xC00000E8ULL;
loc_00B15D83:
    local_rsp = (local_rsp) + (80);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x50` | `32` | `R` |
| `Arg2` | `+ 0x50` | `32` | `W` |
| `Arg2` | `+ 0x54` | `32` | `R` |
| `Arg2` | `+ 0xB8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00B15D50&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B15D50[BB_00B15D50]
  bb_00B15D60[BB_00B15D60]
  bb_00B15D67[BB_00B15D67]
  bb_00B15D7C[BB_00B15D7C]
  bb_00B15D83[BB_00B15D83]
  bb_00B15D89[BB_00B15D89]
  bb_00B15D50 -->|branch| bb_00B15D7C
  bb_00B15D50 -->|fallthrough| bb_00B15D60
  bb_00B15D60 -->|branch| bb_00B15D83
  bb_00B15D60 -->|fallthrough| bb_00B15D67
  bb_00B15D67 -->|branch| bb_00B15D83
  bb_00B15D7C -->|flow| bb_00B15D83
```
