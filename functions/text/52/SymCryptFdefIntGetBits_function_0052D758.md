# SymCryptFdefIntGetBits

- RVA: `0x0052D758`–`0x0052D7B1` (길이 `89` bytes)
- VA: `0x000000014052D758`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `30`개 명령, `89/89` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [SymCryptIntGetBits](SymCryptIntGetBits_function_00525638.md) at `0x0052563C`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0052D758  4C 8B D1                        mov r10, rcx
0052D75B  8B C2                           mov eax, edx
0052D75D  48 C1 E8 05                     shr rax, 5
0052D761  41 83 CB FF                     or r11d, 0xffffffff
0052D765  41 B9 20 00 00 00               mov r9d, 0x20
0052D76B  41 8B C9                        mov ecx, r9d
0052D76E  41 2B C8                        sub ecx, r8d
0052D771  44 8B C2                        mov r8d, edx
0052D774  41 8B 44 82 20                  mov eax, dword ptr [r10 + rax*4 + 0x20]
0052D779  41 83 E0 1F                     and r8d, 0x1f
0052D77D  41 D3 EB                        shr r11d, cl
0052D780  41 8B C8                        mov ecx, r8d
0052D783  D3 E8                           shr eax, cl
0052D785  45 85 C0                        test r8d, r8d
0052D788  74 22                           je 0x14052d7ac
0052D78A  C1 EA 05                        shr edx, 5
0052D78D  8D 4A 01                        lea ecx, [rdx + 1]
0052D790  41 8B 52 04                     mov edx, dword ptr [r10 + 4]
0052D794  C1 E2 04                        shl edx, 4
0052D797  3B CA                           cmp ecx, edx
0052D799  73 11                           jae 0x14052d7ac
0052D79B  8B D1                           mov edx, ecx
0052D79D  45 2B C8                        sub r9d, r8d
0052D7A0  41 8A C9                        mov cl, r9b
0052D7A3  41 8B 54 92 20                  mov edx, dword ptr [r10 + rdx*4 + 0x20]
0052D7A8  D3 E2                           shl edx, cl
0052D7AA  0B C2                           or eax, edx
0052D7AC  41 23 C3                        and eax, r11d
0052D7AF  C3                              ret
0052D7B0  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SymCryptFdefIntGetBits(__int64 a1, int a2, int a3)
{
    __int64 result;
    __int64 v_r11;

    result = ((unsigned int)(a2)) >> (5);
    v_r11 = (unsigned int)((v_r11) | (0xFFFFFFFFULL));
    a1 = (unsigned int)((32) - (a3));
    a3 = (unsigned int)(((unsigned int)(a2)) & (31));
    v_r11 = (unsigned int)((v_r11) >> ((unsigned __int8)(a1)));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + result * 4 + 32))) >> ((unsigned __int8)((unsigned int)(a3))));
    if (a3 == 0) goto loc_0052D7AC;
    a2 = (unsigned int)((a2) >> (5));
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 4))) << (4));
    if (((unsigned int)(a2 + 1)) < a2) {
        a2 = (unsigned int)(a2 + 1);
        a4 = (unsigned int)((32) - (a3));
        a1 = (unsigned __int8)(a4);
        a2 = *(unsigned int *)(a1 + a2 * 4 + 32);
        a2 = (unsigned int)((a2) << ((unsigned __int8)(a1)));
        result = (unsigned int)((result) | (a2));
    }
    result = (unsigned int)((result) & ((unsigned int)(v_r11)));
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t SymCryptFdefIntGetBits(void *Arg1, int32_t Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r11;

    result = ((uint32_t)(Arg2)) >> (5);
    local_r11 = (uint32_t)((local_r11) | (0xFFFFFFFFULL));
    Arg1 = (uint32_t)((32) - (Arg3));
    Arg3 = (uint32_t)(((uint32_t)(Arg2)) & (31));
    local_r11 = (uint32_t)((local_r11) >> ((uint8_t)(Arg1)));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + result * 4 + 0x20))) >> ((uint8_t)((uint32_t)(Arg3))));
    if (Arg3 == 0) goto loc_0052D7AC;
    Arg2 = (uint32_t)((Arg2) >> (5));
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x4))) << (4));
    if (((uint32_t)(Arg2 + 1)) < Arg2) {
        Arg2 = (uint32_t)(Arg2 + 1);
        a4 = (uint32_t)((32) - (Arg3));
        Arg1 = (uint8_t)(a4);
        Arg2 = *(uint32_t *)(arg1 + Arg2 * 4 + 0x20);
        Arg2 = (uint32_t)((Arg2) << ((uint8_t)(Arg1)));
        result = (uint32_t)((result) | (Arg2));
    }
    result = (uint32_t)((result) & ((uint32_t)(local_r11)));
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x4` | `32` | `R` |
| `Arg1` | `+ 0x20 + rax*4` | `32` | `R` |
| `Arg1` | `+ 0x20 + rdx*4` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0052D758&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0052D758[BB_0052D758]
  bb_0052D78A[BB_0052D78A]
  bb_0052D79B[BB_0052D79B]
  bb_0052D7AC[BB_0052D7AC]
  bb_0052D7B0[BB_0052D7B0]
  bb_0052D758 -->|branch| bb_0052D7AC
  bb_0052D758 -->|fallthrough| bb_0052D78A
  bb_0052D78A -->|branch| bb_0052D7AC
  bb_0052D78A -->|fallthrough| bb_0052D79B
  bb_0052D79B -->|flow| bb_0052D7AC
```
