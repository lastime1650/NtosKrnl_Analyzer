# I_MinCryptGetPlatformManifestBinaryIDAttribute

- RVA: `0x00837E9C`–`0x00837F24` (길이 `136` bytes)
- VA: `0x0000000140837E9C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BB544`
- 디코드: `38`개 명령, `136/136` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00837ED6` → [I_MinAsn1ParseSingleAttribute](I_MinAsn1ParseSingleAttribute_function_00838A10.md) (function, `0x00838A10`)
- `0x00837EEE` → [MinAsn1ExtractContent](MinAsn1ExtractContent_function_0083A00C.md) (function, `0x0083A00C`)
- `0x00837F11` → [I_Base64Decode](I_Base64Decode_function_00837CBC.md) (function, `0x00837CBC`)

### Direct callers
- [MinCrypK_VerifySignedDataKModeEx](MinCrypK_VerifySignedDataKModeEx_function_00838568.md) at `0x008387A0`

### Static image references
- `0x00837EC3` → RVA `0x00B4BC18` (`PAGE`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00837E9C  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00837EA1  55                              push rbp
00837EA2  48 8B EC                        mov rbp, rsp
00837EA5  48 83 EC 40                     sub rsp, 0x40
00837EA9  48 8B 42 10                     mov rax, qword ptr [rdx + 0x10]
00837EAD  4C 8D 4D F0                     lea r9, [rbp - 0x10]
00837EB1  48 83 65 28 00                  and qword ptr [rbp + 0x28], 0
00837EB6  0F 57 C0                        xorps xmm0, xmm0
00837EB9  83 65 18 00                     and dword ptr [rbp + 0x18], 0
00837EBD  48 8B DA                        mov rbx, rdx
00837EC0  48 8B D1                        mov rdx, rcx
00837EC3  48 8D 0D 4E 3D 31 00            lea rcx, [rip + 0x313d4e]
00837ECA  0F 11 40 48                     movups xmmword ptr [rax + 0x48], xmm0
00837ECE  0F 11 40 58                     movups xmmword ptr [rax + 0x58], xmm0
00837ED2  0F 11 45 F0                     movups xmmword ptr [rbp - 0x10], xmm0
00837ED6  E8 35 0B 00 00                  call 0x140838a10
00837EDB  84 C0                           test al, al
00837EDD  74 37                           je 0x140837f16
00837EDF  8B 55 F0                        mov edx, dword ptr [rbp - 0x10]
00837EE2  4C 8D 4D 28                     lea r9, [rbp + 0x28]
00837EE6  48 8B 4D F8                     mov rcx, qword ptr [rbp - 8]
00837EEA  4C 8D 45 18                     lea r8, [rbp + 0x18]
00837EEE  E8 19 21 00 00                  call 0x14083a00c
00837EF3  85 C0                           test eax, eax
00837EF5  78 1F                           js 0x140837f16
00837EF7  4C 8B 43 10                     mov r8, qword ptr [rbx + 0x10]
00837EFB  4C 8D 4D 20                     lea r9, [rbp + 0x20]
00837EFF  8B 55 18                        mov edx, dword ptr [rbp + 0x18]
00837F02  49 83 C0 48                     add r8, 0x48
00837F06  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
00837F0A  C7 45 20 20 00 00 00            mov dword ptr [rbp + 0x20], 0x20
00837F11  E8 A6 FD FF FF                  call 0x140837cbc
00837F16  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
00837F1B  33 C0                           xor eax, eax
00837F1D  48 83 C4 40                     add rsp, 0x40
00837F21  5D                              pop rbp
00837F22  C3                              ret
00837F23  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall I_MinCryptGetPlatformManifestBinaryIDAttribute(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m10;
    unsigned __int64 v_stack_m18;
    unsigned int v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (64);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 16) + 72) = v_xmm0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 16) + 88) = v_xmm0;
    v_stack_m18 = v_xmm0;
    result = I_MinAsn1ParseSingleAttribute(v_rip + 3226958, a1, a3, v_stack_m18);
    if ((unsigned __int8)(result) == 0) goto loc_00837F16;
    result = MinAsn1ExtractContent(v_stack_m10, (unsigned int)(v_stack_m18), v_stack_p10, v_stack_p20);
    if (!(sign_flag)) {
        a3 = *(unsigned __int64 *)(a2 + 16);
        a4 = v_stack_p18;
        a2 = v_stack_p10;
        a3 = (a3) + (72);
        a1 = v_stack_p20;
        v_stack_p18 = 32;
        result = I_Base64Decode(a1, a2, a3, a4);
    }
    result = 0;
    v_rsp = (v_rsp) + (64);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t I_MinCryptGetPlatformManifestBinaryIDAttribute(int64_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m10;
    uint64_t v_stack_m18;
    uint32_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (64);
    *(uint64_t *)(*(uint64_t *)(arg2 + 0x10) + 0x48) = v_xmm0;
    *(uint64_t *)(*(uint64_t *)(arg2 + 0x10) + 0x58) = v_xmm0;
    v_stack_m18 = v_xmm0;
    result = I_MinAsn1ParseSingleAttribute(v_rip + 3226958, Arg1, a3, v_stack_m18);
    if ((uint8_t)(result) == 0) goto loc_00837F16;
    result = MinAsn1ExtractContent(v_stack_m10, (uint32_t)(v_stack_m18), v_stack_p10, v_stack_p20);
    if (!(sign_flag)) {
        a3 = *(uint64_t *)(arg2 + 0x10);
        a4 = v_stack_p18;
        Arg2 = v_stack_p10;
        a3 = (a3) + (72);
        Arg1 = v_stack_p20;
        v_stack_p18 = 32;
        result = I_Base64Decode(Arg1, Arg2, a3, a4);
    }
    result = 0;
    local_rsp = (local_rsp) + (64);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x10` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00837E9C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00837E9C[BB_00837E9C]
  bb_00837EDF[BB_00837EDF]
  bb_00837EF7[BB_00837EF7]
  bb_00837F16[BB_00837F16]
  bb_00837F23[BB_00837F23]
  bb_00837E9C -->|branch| bb_00837F16
  bb_00837E9C -->|fallthrough| bb_00837EDF
  bb_00837EDF -->|branch| bb_00837F16
  bb_00837EDF -->|fallthrough| bb_00837EF7
  bb_00837EF7 -->|flow| bb_00837F16
```
