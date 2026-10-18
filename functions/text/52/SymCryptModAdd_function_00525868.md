# SymCryptModAdd

- RVA: `0x00525868`–`0x0052589D` (길이 `53` bytes)
- VA: `0x0000000140525868`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005D2F4`
- 디코드: `14`개 명령, `53/53` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **11**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00525892` → `indirect target` (indirect, 간접 대상)

### Direct callers
- [SymCryptEcurveInitialize](SymCryptEcurveInitialize_function_005241A4.md) at `0x00524664`
- [SymCryptEcDsaSignEx](SymCryptEcDsaSignEx_function_00525D6C.md) at `0x005261B6`
- [SymCryptEcDsaSignEx](SymCryptEcDsaSignEx_function_00525D6C.md) at `0x00526200`
- [SymCryptShortWeierstrassAddDiffNonZero](../53/SymCryptShortWeierstrassAddDiffNonZero_function_00537D80.md) at `0x00537F33`
- [SymCryptShortWeierstrassAddDiffNonZero](../53/SymCryptShortWeierstrassAddDiffNonZero_function_00537D80.md) at `0x0053800B`
- [SymCryptShortWeierstrassAddDiffNonZero](../53/SymCryptShortWeierstrassAddDiffNonZero_function_00537D80.md) at `0x0053813D`
- [SymCryptShortWeierstrassAddSideChannelUnsafe](../53/SymCryptShortWeierstrassAddSideChannelUnsafe_function_00538188.md) at `0x00538449`
- [SymCryptShortWeierstrassAddSideChannelUnsafe](../53/SymCryptShortWeierstrassAddSideChannelUnsafe_function_00538188.md) at `0x005384B9`
- [SymCryptShortWeierstrassAddSideChannelUnsafe](../53/SymCryptShortWeierstrassAddSideChannelUnsafe_function_00538188.md) at `0x0053850A`
- [SymCryptShortWeierstrassAddSideChannelUnsafe](../53/SymCryptShortWeierstrassAddSideChannelUnsafe_function_00538188.md) at `0x00538529`
- [SymCryptShortWeierstrassAddSideChannelUnsafe](../53/SymCryptShortWeierstrassAddSideChannelUnsafe_function_00538188.md) at `0x00538545`
- [SymCryptShortWeierstrassAddSideChannelUnsafe](../53/SymCryptShortWeierstrassAddSideChannelUnsafe_function_00538188.md) at `0x005385EE`
- [SymCryptShortWeierstrassAddSideChannelUnsafe](../53/SymCryptShortWeierstrassAddSideChannelUnsafe_function_00538188.md) at `0x0053860D`
- [SymCryptShortWeierstrassAddSideChannelUnsafe](../53/SymCryptShortWeierstrassAddSideChannelUnsafe_function_00538188.md) at `0x0053862C`
- [SymCryptShortWeierstrassAddSideChannelUnsafe](../53/SymCryptShortWeierstrassAddSideChannelUnsafe_function_00538188.md) at `0x00538667`
- [SymCryptShortWeierstrassAddSideChannelUnsafe](../53/SymCryptShortWeierstrassAddSideChannelUnsafe_function_00538188.md) at `0x00538701`
- [SymCryptShortWeierstrassAddSideChannelUnsafe](../53/SymCryptShortWeierstrassAddSideChannelUnsafe_function_00538188.md) at `0x0053878A`
- [SymCryptShortWeierstrassAddSideChannelUnsafe](../53/SymCryptShortWeierstrassAddSideChannelUnsafe_function_00538188.md) at `0x005387A6`
- [SymCryptShortWeierstrassAddSideChannelUnsafe](../53/SymCryptShortWeierstrassAddSideChannelUnsafe_function_00538188.md) at `0x005388D0`
- [SymCryptShortWeierstrassDouble](../53/SymCryptShortWeierstrassDouble_function_00538960.md) at `0x00538A43`
- [SymCryptShortWeierstrassDouble](../53/SymCryptShortWeierstrassDouble_function_00538960.md) at `0x00538AB5`
- [SymCryptShortWeierstrassDouble](../53/SymCryptShortWeierstrassDouble_function_00538960.md) at `0x00538B5A`
- [SymCryptShortWeierstrassDouble](../53/SymCryptShortWeierstrassDouble_function_00538960.md) at `0x00538B75`
- [SymCryptShortWeierstrassDouble](../53/SymCryptShortWeierstrassDouble_function_00538960.md) at `0x00538B95`
- [SymCryptShortWeierstrassDouble](../53/SymCryptShortWeierstrassDouble_function_00538960.md) at `0x00538BB0`
- [SymCryptShortWeierstrassDoubleSpecializedAm3](../53/SymCryptShortWeierstrassDoubleSpecializedAm3_function_00538C70.md) at `0x00538D4A`
- [SymCryptShortWeierstrassDoubleSpecializedAm3](../53/SymCryptShortWeierstrassDoubleSpecializedAm3_function_00538C70.md) at `0x00538DBC`
- [SymCryptShortWeierstrassDoubleSpecializedAm3](../53/SymCryptShortWeierstrassDoubleSpecializedAm3_function_00538C70.md) at `0x00538DDE`
- [SymCryptShortWeierstrassDoubleSpecializedAm3](../53/SymCryptShortWeierstrassDoubleSpecializedAm3_function_00538C70.md) at `0x00538E69`
- [SymCryptShortWeierstrassDoubleSpecializedAm3](../53/SymCryptShortWeierstrassDoubleSpecializedAm3_function_00538C70.md) at `0x00538E84`
- [SymCryptShortWeierstrassDoubleSpecializedAm3](../53/SymCryptShortWeierstrassDoubleSpecializedAm3_function_00538C70.md) at `0x00538E9F`
- [SymCryptShortWeierstrassOnCurve](../53/SymCryptShortWeierstrassOnCurve_function_00539420.md) at `0x0053955D`
- [SymCryptShortWeierstrassOnCurve](../53/SymCryptShortWeierstrassOnCurve_function_00539420.md) at `0x005395A9`
- [SymCryptTwistedEdwardsAdd](../53/SymCryptTwistedEdwardsAdd_function_005396D0.md) at `0x005398D3`
- [SymCryptTwistedEdwardsAdd](../53/SymCryptTwistedEdwardsAdd_function_005396D0.md) at `0x00539909`
- [SymCryptTwistedEdwardsAdd](../53/SymCryptTwistedEdwardsAdd_function_005396D0.md) at `0x005399A7`
- [SymCryptTwistedEdwardsDouble](../53/SymCryptTwistedEdwardsDouble_function_00539AF0.md) at `0x00539C36`
- [SymCryptTwistedEdwardsDouble](../53/SymCryptTwistedEdwardsDouble_function_00539AF0.md) at `0x00539C92`
- [SymCryptTwistedEdwardsDouble](../53/SymCryptTwistedEdwardsDouble_function_00539AF0.md) at `0x00539D16`
- [SymCryptTwistedEdwardsOnCurve](../53/SymCryptTwistedEdwardsOnCurve_function_0053A310.md) at `0x0053A42C`
- [SymCryptTwistedEdwardsOnCurve](../53/SymCryptTwistedEdwardsOnCurve_function_0053A310.md) at `0x0053A4B7`
- [SymCryptMontgomeryDoubleAndAdd](../53/SymCryptMontgomeryDoubleAndAdd_function_0053A5AC.md) at `0x0053A609`
- [SymCryptMontgomeryDoubleAndAdd](../53/SymCryptMontgomeryDoubleAndAdd_function_0053A5AC.md) at `0x0053A654`
- [SymCryptMontgomeryDoubleAndAdd](../53/SymCryptMontgomeryDoubleAndAdd_function_0053A5AC.md) at `0x0053A781`
- [SymCryptMontgomeryDoubleAndAdd](../53/SymCryptMontgomeryDoubleAndAdd_function_0053A5AC.md) at `0x0053A7BF`

### Static image references
- `0x0052586E` → RVA `0x000067D0` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00525868  48 83 EC 38                     sub rsp, 0x38
0052586C  8B 01                           mov eax, dword ptr [rcx]
0052586E  4C 8D 15 5B 0F AE FF            lea r10, [rip - 0x51f0a5]
00525875  25 80 03 00 00                  and eax, 0x380
0052587A  4A 8B 04 10                     mov rax, qword ptr [rax + r10]
0052587E  4C 8B 54 24 68                  mov r10, qword ptr [rsp + 0x68]
00525883  4C 89 54 24 28                  mov qword ptr [rsp + 0x28], r10
00525888  4C 8B 54 24 60                  mov r10, qword ptr [rsp + 0x60]
0052588D  4C 89 54 24 20                  mov qword ptr [rsp + 0x20], r10
00525892  FF D0                           call rax
00525894  0F 1F 00                        nop dword ptr [rax]
00525897  48 83 C4 38                     add rsp, 0x38
0052589B  C3                              ret
0052589C  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SymCryptModAdd(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m10;
    unsigned __int64 v_stack_m18;

    v_rsp = (v_rsp) - (56);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1))) & (896));
    v_stack_m10 = a6;
    v_stack_m18 = a5;
    result = kernel_indirect_call(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (56);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t SymCryptModAdd(void *Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, int64_t Arg5, int64_t Arg6)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m10;
    uint64_t v_stack_m18;

    local_rsp = (local_rsp) - (56);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1))) & (896));
    v_stack_m10 = Arg6;
    v_stack_m18 = Arg5;
    result = kernel_indirect_call(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (56);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00525868&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00525868[BB_00525868]
  bb_0052589C[BB_0052589C]
```
