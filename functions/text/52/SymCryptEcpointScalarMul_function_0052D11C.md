# SymCryptEcpointScalarMul

- RVA: `0x0052D11C`–`0x0052D167` (길이 `75` bytes)
- VA: `0x000000014052D11C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00063458`
- 디코드: `19`개 명령, `75/75` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **5**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0052D15C` → `indirect target` (indirect, 간접 대상)

### Direct callers
- [SymCryptEckeyPerformPublicKeyValidation](SymCryptEckeyPerformPublicKeyValidation_function_00524B1C.md) at `0x00524BE3`
- [SymCryptEckeySetValue](SymCryptEckeySetValue_function_00524C34.md) at `0x00525029`
- [SymCryptEcDsaSignEx](SymCryptEcDsaSignEx_function_00525D6C.md) at `0x0052605E`
- [SymCryptEcpointGenericSetRandom](SymCryptEcpointGenericSetRandom_function_0052B850.md) at `0x0052B8F9`
- [SymCryptEcDhSecretAgreement](../53/SymCryptEcDhSecretAgreement_function_00537798.md) at `0x005378D2`

### Static image references
- `0x0052D12E` → RVA `0x00006CD0` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0052D11C  48 83 EC 48                     sub rsp, 0x48
0052D120  8B 41 04                        mov eax, dword ptr [rcx + 4]
0052D123  45 8B D9                        mov r11d, r9d
0052D126  4C 8B 94 24 80 00 00 00         mov r10, qword ptr [rsp + 0x80]
0052D12E  4C 8D 0D 9B 9B AD FF            lea r9, [rip - 0x526465]
0052D135  4C 89 54 24 30                  mov qword ptr [rsp + 0x30], r10
0052D13A  83 E0 07                        and eax, 7
0052D13D  4C 8B 54 24 78                  mov r10, qword ptr [rsp + 0x78]
0052D142  48 C1 E0 07                     shl rax, 7
0052D146  4C 89 54 24 28                  mov qword ptr [rsp + 0x28], r10
0052D14B  4A 8B 04 08                     mov rax, qword ptr [rax + r9]
0052D14F  4C 8B 4C 24 70                  mov r9, qword ptr [rsp + 0x70]
0052D154  4C 89 4C 24 20                  mov qword ptr [rsp + 0x20], r9
0052D159  45 8B CB                        mov r9d, r11d
0052D15C  FF D0                           call rax
0052D15E  0F 1F 00                        nop dword ptr [rax]
0052D161  48 83 C4 48                     add rsp, 0x48
0052D165  C3                              ret
0052D166  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SymCryptEcpointScalarMul(__int64 a1, __int64 a2, __int64 a3, int a4, __int64 a5, __int64 a6, __int64 a7)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m20;
    unsigned __int64 v_stack_m28;

    v_rsp = (v_rsp) - (72);
    v_stack_m18 = a7;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 4))) & (7));
    result = (result) << (7);
    v_stack_m20 = a6;
    v_stack_m28 = a5;
    result = kernel_indirect_call(a1, a2, a3, (unsigned int)((unsigned int)((unsigned int)(a4))));
    v_rsp = (v_rsp) + (72);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t SymCryptEcpointScalarMul(void *Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4, int64_t Arg5, int64_t Arg6, int64_t Arg7)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_m20;
    uint64_t v_stack_m28;

    local_rsp = (local_rsp) - (72);
    v_stack_m18 = Arg7;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x4))) & (7));
    result = (result) << (7);
    v_stack_m20 = Arg6;
    v_stack_m28 = Arg5;
    result = kernel_indirect_call(Arg1, Arg2, Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    local_rsp = (local_rsp) + (72);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x4` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0052D11C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0052D11C[BB_0052D11C]
  bb_0052D166[BB_0052D166]
```
