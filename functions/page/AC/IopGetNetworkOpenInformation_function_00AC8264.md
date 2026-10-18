# IopGetNetworkOpenInformation

- RVA: `0x00AC8264`–`0x00AC837C` (길이 `280` bytes)
- VA: `0x0000000140AC8264`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BE0BC`
- 디코드: `75`개 명령, `280/280` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00AC82C8` → [IopQueryXxxInformation](../8A/IopQueryXxxInformation_function_008A89D0.md) (function, `0x008A89D0`)
- `0x00AC82FC` → [IopQueryXxxInformation](../8A/IopQueryXxxInformation_function_008A89D0.md) (function, `0x008A89D0`)
- `0x00AC8361` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [IopParseDevice](../89/IopParseDevice_function_0089E510.md) at `0x0089F0BD`

### Static image references
- `0x00AC827B` → RVA `0x00E0A740` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00AC8361` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00AC8264  4C 8B DC                        mov r11, rsp
00AC8267  49 89 5B 18                     mov qword ptr [r11 + 0x18], rbx
00AC826B  49 89 7B 20                     mov qword ptr [r11 + 0x20], rdi
00AC826F  55                              push rbp
00AC8270  49 8D 6B A1                     lea rbp, [r11 - 0x5f]
00AC8274  48 81 EC 90 00 00 00            sub rsp, 0x90
00AC827B  48 8B 05 BE 24 34 00            mov rax, qword ptr [rip + 0x3424be]
00AC8282  48 33 C4                        xor rax, rsp
00AC8285  48 89 45 4F                     mov qword ptr [rbp + 0x4f], rax
00AC8289  33 C0                           xor eax, eax
00AC828B  C6 44 24 30 01                  mov byte ptr [rsp + 0x30], 1
00AC8290  0F 57 C0                        xorps xmm0, xmm0
00AC8293  48 89 45 2F                     mov qword ptr [rbp + 0x2f], rax
00AC8297  48 89 45 47                     mov qword ptr [rbp + 0x47], rax
00AC829B  45 33 C9                        xor r9d, r9d
00AC829E  48 8D 45 07                     lea rax, [rbp + 7]
00AC82A2  48 8B DA                        mov rbx, rdx
00AC82A5  49 89 43 90                     mov qword ptr [r11 - 0x70], rax
00AC82A9  48 8B F9                        mov rdi, rcx
00AC82AC  48 8D 45 0F                     lea rax, [rbp + 0xf]
00AC82B0  41 8D 51 04                     lea edx, [r9 + 4]
00AC82B4  49 89 43 88                     mov qword ptr [r11 - 0x78], rax
00AC82B8  45 8D 41 28                     lea r8d, [r9 + 0x28]
00AC82BC  0F 11 45 0F                     movups xmmword ptr [rbp + 0xf], xmm0
00AC82C0  0F 11 45 1F                     movups xmmword ptr [rbp + 0x1f], xmm0
00AC82C4  0F 11 45 37                     movups xmmword ptr [rbp + 0x37], xmm0
00AC82C8  E8 03 07 DE FF                  call 0x1408a89d0
00AC82CD  8B D0                           mov edx, eax
00AC82CF  85 C0                           test eax, eax
00AC82D1  0F 88 81 00 00 00               js 0x140ac8358
00AC82D7  45 33 C9                        xor r9d, r9d
00AC82DA  C6 44 24 30 01                  mov byte ptr [rsp + 0x30], 1
00AC82DF  48 8D 45 07                     lea rax, [rbp + 7]
00AC82E3  48 8B CF                        mov rcx, rdi
00AC82E6  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AC82EB  48 8D 45 37                     lea rax, [rbp + 0x37]
00AC82EF  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AC82F4  41 8D 51 05                     lea edx, [r9 + 5]
00AC82F8  45 8D 41 18                     lea r8d, [r9 + 0x18]
00AC82FC  E8 CF 06 DE FF                  call 0x1408a89d0
00AC8301  8B D0                           mov edx, eax
00AC8303  85 C0                           test eax, eax
00AC8305  78 51                           js 0x140ac8358
00AC8307  48 8B 4B 68                     mov rcx, qword ptr [rbx + 0x68]
00AC830B  48 8B 45 0F                     mov rax, qword ptr [rbp + 0xf]
00AC830F  48 89 01                        mov qword ptr [rcx], rax
00AC8312  48 8B 4B 68                     mov rcx, qword ptr [rbx + 0x68]
00AC8316  48 8B 45 17                     mov rax, qword ptr [rbp + 0x17]
00AC831A  48 89 41 08                     mov qword ptr [rcx + 8], rax
00AC831E  48 8B 4B 68                     mov rcx, qword ptr [rbx + 0x68]
00AC8322  48 8B 45 1F                     mov rax, qword ptr [rbp + 0x1f]
00AC8326  48 89 41 10                     mov qword ptr [rcx + 0x10], rax
00AC832A  48 8B 4B 68                     mov rcx, qword ptr [rbx + 0x68]
00AC832E  48 8B 45 27                     mov rax, qword ptr [rbp + 0x27]
00AC8332  48 89 41 18                     mov qword ptr [rcx + 0x18], rax
00AC8336  48 8B 4B 68                     mov rcx, qword ptr [rbx + 0x68]
00AC833A  48 8B 45 37                     mov rax, qword ptr [rbp + 0x37]
00AC833E  48 89 41 20                     mov qword ptr [rcx + 0x20], rax
00AC8342  48 8B 4B 68                     mov rcx, qword ptr [rbx + 0x68]
00AC8346  48 8B 45 3F                     mov rax, qword ptr [rbp + 0x3f]
00AC834A  48 89 41 28                     mov qword ptr [rcx + 0x28], rax
00AC834E  48 8B 4B 68                     mov rcx, qword ptr [rbx + 0x68]
00AC8352  8B 45 2F                        mov eax, dword ptr [rbp + 0x2f]
00AC8355  89 41 30                        mov dword ptr [rcx + 0x30], eax
00AC8358  8B C2                           mov eax, edx
00AC835A  48 8B 4D 4F                     mov rcx, qword ptr [rbp + 0x4f]
00AC835E  48 33 CC                        xor rcx, rsp
00AC8361  E8 DA 42 BE FF                  call 0x1406ac640
00AC8366  4C 8D 9C 24 90 00 00 00         lea r11, [rsp + 0x90]
00AC836E  49 8B 5B 20                     mov rbx, qword ptr [r11 + 0x20]
00AC8372  49 8B 7B 28                     mov rdi, qword ptr [r11 + 0x28]
00AC8376  49 8B E3                        mov rsp, r11
00AC8379  5D                              pop rbp
00AC837A  C3                              ret
00AC837B  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IopGetNetworkOpenInformation(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int8 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m8;

    *(unsigned __int64 *)(v_rsp + 24) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    v_rsp = (v_rsp) - (144);
    result = (*(unsigned __int64 *)(v_rip + 3417278)) ^ (v_rsp);
    *(unsigned __int64 *)(v_rsp - 95 + 79) = result;
    result = 0;
    v_stack_m68 = 1;
    *(unsigned __int64 *)(v_rsp - 95 + 47) = 0;
    *(unsigned __int64 *)(v_rsp - 95 + 71) = 0;
    a4 = 0;
    *(unsigned __int64 *)(v_rsp - 112) = v_rsp - 95 + 7;
    *(unsigned __int64 *)(v_rsp - 120) = v_rsp - 95 + 15;
    *(unsigned __int64 *)(v_rsp - 95 + 15) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 95 + 31) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 95 + 55) = v_xmm0;
    result = IopQueryXxxInformation(a1, a4 + 4, a4 + 40, a4);
    if (sign_flag) goto loc_00AC8358;
    a4 = 0;
    v_stack_m68 = 1;
    v_stack_m70 = v_rsp - 95 + 7;
    v_stack_m78 = v_rsp - 95 + 55;
    result = IopQueryXxxInformation(a1, a4 + 5, a4 + 24, a4);
    if (!(sign_flag)) {
        a1 = *(unsigned __int64 *)(a2 + 104);
        result = *(unsigned __int64 *)(v_rsp - 95 + 15);
        *(unsigned __int64 *)(a1) = result;
        a1 = *(unsigned __int64 *)(a2 + 104);
        result = *(unsigned __int64 *)(v_rsp - 95 + 23);
        *(unsigned __int64 *)(a1 + 8) = result;
        a1 = *(unsigned __int64 *)(a2 + 104);
        result = *(unsigned __int64 *)(v_rsp - 95 + 31);
        *(unsigned __int64 *)(a1 + 16) = result;
        a1 = *(unsigned __int64 *)(a2 + 104);
        result = *(unsigned __int64 *)(v_rsp - 95 + 39);
        *(unsigned __int64 *)(a1 + 24) = result;
        a1 = *(unsigned __int64 *)(a2 + 104);
        result = *(unsigned __int64 *)(v_rsp - 95 + 55);
        *(unsigned __int64 *)(a1 + 32) = result;
        a1 = *(unsigned __int64 *)(a2 + 104);
        result = *(unsigned __int64 *)(v_rsp - 95 + 63);
        *(unsigned __int64 *)(a1 + 40) = result;
        a1 = *(unsigned __int64 *)(a2 + 104);
        result = *(unsigned int *)(v_rsp - 95 + 47);
        *(unsigned int *)(a1 + 48) = (unsigned int)(result);
    }
    a1 = (*(unsigned __int64 *)(v_rsp - 95 + 79)) ^ (v_rsp);
    result = _security_check_cookie(a1, (unsigned int)((unsigned int)(result)), a4 + 24, a4);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t IopGetNetworkOpenInformation(int64_t Arg1, void *Arg2, int64_t Arg3, int32_t Arg4)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;
    uint8_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m8;

    *(uint64_t *)(local_rsp + 0x18) = local_rbx;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    local_rsp = (local_rsp) - (144);
    result = (*(uint64_t *)(v_rip + 0x3424BE)) ^ (local_rsp);
    *(uint64_t *)(local_rsp - 0x5F + 0x4F) = result;
    result = 0;
    v_stack_m68 = 1;
    *(uint64_t *)(local_rsp - 0x5F + 0x2F) = 0;
    *(uint64_t *)(local_rsp - 0x5F + 0x47) = 0;
    Arg4 = 0;
    *(uint64_t *)(local_rsp - 0x70) = local_rsp - 95 + 7;
    *(uint64_t *)(local_rsp - 0x78) = local_rsp - 95 + 15;
    *(uint64_t *)(local_rsp - 0x5F + 0xF) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x5F + 0x1F) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x5F + 0x37) = v_xmm0;
    result = IopQueryXxxInformation(Arg1, Arg4 + 4, Arg4 + 40, Arg4);
    if (sign_flag) goto loc_00AC8358;
    Arg4 = 0;
    v_stack_m68 = 1;
    v_stack_m70 = local_rsp - 95 + 7;
    v_stack_m78 = local_rsp - 95 + 55;
    result = IopQueryXxxInformation(Arg1, Arg4 + 5, Arg4 + 24, Arg4);
    if (!(sign_flag)) {
        Arg1 = *(uint64_t *)(arg2 + 0x68);
        result = *(uint64_t *)(local_rsp - 0x5F + 0xF);
        *(uint64_t *)(Arg1) = result;
        Arg1 = *(uint64_t *)(arg2 + 0x68);
        result = *(uint64_t *)(local_rsp - 0x5F + 0x17);
        *(uint64_t *)(Arg1 + 0x8) = result;
        Arg1 = *(uint64_t *)(arg2 + 0x68);
        result = *(uint64_t *)(local_rsp - 0x5F + 0x1F);
        *(uint64_t *)(Arg1 + 0x10) = result;
        Arg1 = *(uint64_t *)(arg2 + 0x68);
        result = *(uint64_t *)(local_rsp - 0x5F + 0x27);
        *(uint64_t *)(Arg1 + 0x18) = result;
        Arg1 = *(uint64_t *)(arg2 + 0x68);
        result = *(uint64_t *)(local_rsp - 0x5F + 0x37);
        *(uint64_t *)(Arg1 + 0x20) = result;
        Arg1 = *(uint64_t *)(arg2 + 0x68);
        result = *(uint64_t *)(local_rsp - 0x5F + 0x3F);
        *(uint64_t *)(Arg1 + 0x28) = result;
        Arg1 = *(uint64_t *)(arg2 + 0x68);
        result = *(uint32_t *)(local_rsp - 0x5F + 0x2F);
        *(uint32_t *)(Arg1 + 0x30) = (uint32_t)(result);
    }
    Arg1 = (*(uint64_t *)(local_rsp - 0x5F + 0x4F)) ^ (local_rsp);
    result = _security_check_cookie(Arg1, (uint32_t)((uint32_t)(result)), Arg4 + 24, Arg4);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x68` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00AC8264&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00AC8264[BB_00AC8264]
  bb_00AC82D7[BB_00AC82D7]
  bb_00AC8307[BB_00AC8307]
  bb_00AC8358[BB_00AC8358]
  bb_00AC837B[BB_00AC837B]
  bb_00AC8264 -->|branch| bb_00AC8358
  bb_00AC8264 -->|fallthrough| bb_00AC82D7
  bb_00AC82D7 -->|branch| bb_00AC8358
  bb_00AC82D7 -->|fallthrough| bb_00AC8307
  bb_00AC8307 -->|flow| bb_00AC8358
```
