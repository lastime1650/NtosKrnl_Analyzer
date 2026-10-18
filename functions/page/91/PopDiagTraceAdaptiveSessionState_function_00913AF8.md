# PopDiagTraceAdaptiveSessionState

- RVA: `0x00913AF8`–`0x00913C49` (길이 `337` bytes)
- VA: `0x0000000140913AF8`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008A514`
- 디코드: `79`개 명령, `337/337` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x00913B42` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (function, `0x00392450`)
- `0x00913C26` → [EtwWrite](../../text/41/EtwWrite_function_0041C720.md) (function, `0x0041C720`)
- `0x00913C32` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [PopAdaptiveGetSessionStateUnsafe](PopAdaptiveGetSessionStateUnsafe_function_00913A4C.md) at `0x00913AC4`

### Static image references
- `0x00913B16` → RVA `0x00E0A740` (`.data`; read)
- `0x00913B24` → RVA `0x00E67858` (`.data`; read)
- `0x00913B34` → RVA `0x00F0B408` (`.data`; read)
- `0x00913B3B` → RVA `0x00011A48` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x00913B42` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (`PAGE` → `.text`)
  - `0x00913C26` → [EtwWrite](../../text/41/EtwWrite_function_0041C720.md) (`PAGE` → `.text`)
  - `0x00913C32` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00913AF8  48 8B C4                        mov rax, rsp
00913AFB  48 89 58 20                     mov qword ptr [rax + 0x20], rbx
00913AFF  4C 89 40 18                     mov qword ptr [rax + 0x18], r8
00913B03  48 89 50 10                     mov qword ptr [rax + 0x10], rdx
00913B07  89 48 08                        mov dword ptr [rax + 8], ecx
00913B0A  55                              push rbp
00913B0B  48 8D 68 D1                     lea rbp, [rax - 0x2f]
00913B0F  48 81 EC F0 00 00 00            sub rsp, 0xf0
00913B16  48 8B 05 23 6C 4F 00            mov rax, qword ptr [rip + 0x4f6c23]
00913B1D  48 33 C4                        xor rax, rsp
00913B20  48 89 45 17                     mov qword ptr [rbp + 0x17], rax
00913B24  80 3D 2D 3D 55 00 00            cmp byte ptr [rip + 0x553d2d], 0
00913B2B  41 8B D9                        mov ebx, r9d
00913B2E  0F 84 F7 00 00 00               je 0x140913c2b
00913B34  48 8B 0D CD 78 5F 00            mov rcx, qword ptr [rip + 0x5f78cd]
00913B3B  48 8D 15 06 DF 6F FF            lea rdx, [rip - 0x9020fa]
00913B42  E8 09 E9 A7 FF                  call 0x140392450
00913B47  84 C0                           test al, al
00913B49  0F 84 DC 00 00 00               je 0x140913c2b
00913B4F  0F B6 45 67                     movzx eax, byte ptr [rbp + 0x67]
00913B53  48 8D 15 EE DE 6F FF            lea rdx, [rip - 0x902112]
00913B5A  83 65 83 00                     and dword ptr [rbp - 0x7d], 0
00913B5E  41 B8 04 00 00 00               mov r8d, 4
00913B64  83 65 93 00                     and dword ptr [rbp - 0x6d], 0
00913B68  83 65 A3 00                     and dword ptr [rbp - 0x5d], 0
00913B6C  83 65 B3 00                     and dword ptr [rbp - 0x4d], 0
00913B70  83 65 C3 00                     and dword ptr [rbp - 0x3d], 0
00913B74  41 8D 48 04                     lea ecx, [r8 + 4]
00913B78  83 65 D3 00                     and dword ptr [rbp - 0x2d], 0
00913B7C  45 8D 48 06                     lea r9d, [r8 + 6]
00913B80  83 65 E3 00                     and dword ptr [rbp - 0x1d], 0
00913B84  83 65 F3 00                     and dword ptr [rbp - 0xd], 0
00913B88  83 65 03 00                     and dword ptr [rbp + 3], 0
00913B8C  83 65 13 00                     and dword ptr [rbp + 0x13], 0
00913B90  89 44 24 34                     mov dword ptr [rsp + 0x34], eax
00913B94  48 8D 45 37                     lea rax, [rbp + 0x37]
00913B98  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00913B9D  48 8D 45 3F                     lea rax, [rbp + 0x3f]
00913BA1  48 89 45 87                     mov qword ptr [rbp - 0x79], rax
00913BA5  48 8D 45 47                     lea rax, [rbp + 0x47]
00913BA9  48 89 45 97                     mov qword ptr [rbp - 0x69], rax
00913BAD  48 8D 44 24 30                  lea rax, [rsp + 0x30]
00913BB2  48 89 45 A7                     mov qword ptr [rbp - 0x59], rax
00913BB6  48 8D 45 57                     lea rax, [rbp + 0x57]
00913BBA  48 89 45 B7                     mov qword ptr [rbp - 0x49], rax
00913BBE  48 8D 45 5F                     lea rax, [rbp + 0x5f]
00913BC2  48 89 45 C7                     mov qword ptr [rbp - 0x39], rax
00913BC6  48 8D 44 24 34                  lea rax, [rsp + 0x34]
00913BCB  48 89 45 D7                     mov qword ptr [rbp - 0x29], rax
00913BCF  48 8D 45 6F                     lea rax, [rbp + 0x6f]
00913BD3  48 89 45 E7                     mov qword ptr [rbp - 0x19], rax
00913BD7  48 8D 45 77                     lea rax, [rbp + 0x77]
00913BDB  48 89 45 F7                     mov qword ptr [rbp - 9], rax
00913BDF  48 8D 45 7F                     lea rax, [rbp + 0x7f]
00913BE3  48 89 45 07                     mov qword ptr [rbp + 7], rax
00913BE7  48 8D 44 24 40                  lea rax, [rsp + 0x40]
00913BEC  44 89 44 24 48                  mov dword ptr [rsp + 0x48], r8d
00913BF1  89 4D 8F                        mov dword ptr [rbp - 0x71], ecx
00913BF4  89 4D 9F                        mov dword ptr [rbp - 0x61], ecx
00913BF7  48 8B 0D 0A 78 5F 00            mov rcx, qword ptr [rip + 0x5f780a]
00913BFE  44 89 45 AF                     mov dword ptr [rbp - 0x51], r8d
00913C02  44 89 45 BF                     mov dword ptr [rbp - 0x41], r8d
00913C06  44 89 45 CF                     mov dword ptr [rbp - 0x31], r8d
00913C0A  44 89 45 DF                     mov dword ptr [rbp - 0x21], r8d
00913C0E  44 89 45 EF                     mov dword ptr [rbp - 0x11], r8d
00913C12  44 89 45 FF                     mov dword ptr [rbp - 1], r8d
00913C16  44 89 45 0F                     mov dword ptr [rbp + 0xf], r8d
00913C1A  45 33 C0                        xor r8d, r8d
00913C1D  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00913C22  89 5C 24 30                     mov dword ptr [rsp + 0x30], ebx
00913C26  E8 F5 8A B0 FF                  call 0x14041c720
00913C2B  48 8B 4D 17                     mov rcx, qword ptr [rbp + 0x17]
00913C2F  48 33 CC                        xor rcx, rsp
00913C32  E8 09 8A D9 FF                  call 0x1406ac640
00913C37  48 8B 9C 24 18 01 00 00         mov rbx, qword ptr [rsp + 0x118]
00913C3F  48 81 C4 F0 00 00 00            add rsp, 0xf0
00913C46  5D                              pop rbp
00913C47  C3                              ret
00913C48  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopDiagTraceAdaptiveSessionState(int a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned int v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned int v_stack_mC4;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_p20;

    *(unsigned __int64 *)(v_rsp + 32) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 24) = a3;
    *(unsigned __int64 *)(v_rsp + 16) = a2;
    *(unsigned int *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (240);
    result = (*(unsigned __int64 *)(v_rip + 5205027)) ^ (v_rsp);
    *(unsigned __int64 *)(v_rsp - 47 + 23) = result;
    if ((*(unsigned __int8 *)(v_rip + 5586221)) == 0) goto loc_00913C2B;
    result = EtwEventEnabled(*(unsigned __int64 *)(v_rip + 6256845), v_rip - 9445626, a3, a4);
    if ((unsigned __int8)(result) != 0) {
        result = *(unsigned __int8 *)(v_rsp - 47 + 103);
        a2 = v_rip - 9445650;
        a3 = 4;
        a1 = a3 + 4;
        a4 = a3 + 6;
        v_stack_mC4 = (unsigned int)(result);
        result = v_rsp - 47 + 55;
        v_stack_mB8 = result;
        result = v_rsp - 47 + 63;
        *(unsigned __int64 *)(v_rsp - 47 - 121) = result;
        result = v_rsp - 47 + 71;
        *(unsigned __int64 *)(v_rsp - 47 - 105) = result;
        result = v_stack_mC8;
        *(unsigned __int64 *)(v_rsp - 47 - 89) = result;
        result = v_rsp - 47 + 87;
        *(unsigned __int64 *)(v_rsp - 47 - 73) = result;
        result = v_rsp - 47 + 95;
        *(unsigned __int64 *)(v_rsp - 47 - 57) = result;
        result = v_stack_mC4;
        *(unsigned __int64 *)(v_rsp - 47 - 41) = result;
        result = v_rsp - 47 + 111;
        *(unsigned __int64 *)(v_rsp - 47 - 25) = result;
        result = v_rsp - 47 + 119;
        *(unsigned __int64 *)(v_rsp - 47 - 9) = result;
        result = v_rsp - 47 + 127;
        *(unsigned __int64 *)(v_rsp - 47 + 7) = result;
        result = v_stack_mB8;
        v_stack_mB0 = (unsigned int)(a3);
        *(unsigned int *)(v_rsp - 47 - 113) = a1;
        *(unsigned int *)(v_rsp - 47 - 97) = a1;
        a1 = *(unsigned __int64 *)(v_rip + 6256650);
        *(unsigned int *)(v_rsp - 47 - 81) = (unsigned int)(a3);
        *(unsigned int *)(v_rsp - 47 - 65) = (unsigned int)(a3);
        *(unsigned int *)(v_rsp - 47 - 49) = (unsigned int)(a3);
        *(unsigned int *)(v_rsp - 47 - 33) = (unsigned int)(a3);
        *(unsigned int *)(v_rsp - 47 - 17) = (unsigned int)(a3);
        *(unsigned int *)(v_rsp - 47 - 1) = (unsigned int)(a3);
        *(unsigned int *)(v_rsp - 47 + 15) = (unsigned int)(a3);
        a3 = 0;
        v_stack_mD8 = result;
        v_stack_mC8 = (unsigned int)((unsigned int)(a4));
        result = EtwWrite(a1, a2, a3, a4);
    }
    a1 = (*(unsigned __int64 *)(v_rsp - 47 + 23)) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (240);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PopDiagTraceAdaptiveSessionState(int32_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint32_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint32_t v_stack_mC4;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD8;
    uint64_t v_stack_p20;

    *(uint64_t *)(local_rsp + 0x20) = local_rbx;
    *(uint64_t *)(local_rsp + 0x18) = Arg3;
    *(uint64_t *)(local_rsp + 0x10) = Arg2;
    *(uint32_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (240);
    result = (*(uint64_t *)(v_rip + 0x4F6C23)) ^ (local_rsp);
    *(uint64_t *)(local_rsp - 0x2F + 0x17) = result;
    if ((*(uint8_t *)(v_rip + 0x553D2D)) == 0) goto loc_00913C2B;
    result = EtwEventEnabled(*(uint64_t *)(v_rip + 0x5F78CD), v_rip - 9445626, Arg3, Arg4);
    if ((uint8_t)(result) != 0) {
        result = *(uint8_t *)(local_rsp - 0x2F + 0x67);
        Arg2 = v_rip - 9445650;
        Arg3 = 4;
        Arg1 = Arg3 + 4;
        Arg4 = Arg3 + 6;
        v_stack_mC4 = (uint32_t)(result);
        result = local_rsp - 47 + 55;
        v_stack_mB8 = result;
        result = local_rsp - 47 + 63;
        *(uint64_t *)(local_rsp - 0x2F - 0x79) = result;
        result = local_rsp - 47 + 71;
        *(uint64_t *)(local_rsp - 0x2F - 0x69) = result;
        result = v_stack_mC8;
        *(uint64_t *)(local_rsp - 0x2F - 0x59) = result;
        result = local_rsp - 47 + 87;
        *(uint64_t *)(local_rsp - 0x2F - 0x49) = result;
        result = local_rsp - 47 + 95;
        *(uint64_t *)(local_rsp - 0x2F - 0x39) = result;
        result = v_stack_mC4;
        *(uint64_t *)(local_rsp - 0x2F - 0x29) = result;
        result = local_rsp - 47 + 111;
        *(uint64_t *)(local_rsp - 0x2F - 0x19) = result;
        result = local_rsp - 47 + 119;
        *(uint64_t *)(local_rsp - 0x2F - 0x9) = result;
        result = local_rsp - 47 + 127;
        *(uint64_t *)(local_rsp - 0x2F + 0x7) = result;
        result = v_stack_mB8;
        v_stack_mB0 = (uint32_t)(Arg3);
        *(uint32_t *)(local_rsp - 0x2F - 0x71) = Arg1;
        *(uint32_t *)(local_rsp - 0x2F - 0x61) = Arg1;
        Arg1 = *(uint64_t *)(v_rip + 0x5F780A);
        *(uint32_t *)(local_rsp - 0x2F - 0x51) = (uint32_t)(Arg3);
        *(uint32_t *)(local_rsp - 0x2F - 0x41) = (uint32_t)(Arg3);
        *(uint32_t *)(local_rsp - 0x2F - 0x31) = (uint32_t)(Arg3);
        *(uint32_t *)(local_rsp - 0x2F - 0x21) = (uint32_t)(Arg3);
        *(uint32_t *)(local_rsp - 0x2F - 0x11) = (uint32_t)(Arg3);
        *(uint32_t *)(local_rsp - 0x2F - 0x1) = (uint32_t)(Arg3);
        *(uint32_t *)(local_rsp - 0x2F + 0xF) = (uint32_t)(Arg3);
        Arg3 = 0;
        v_stack_mD8 = result;
        v_stack_mC8 = (uint32_t)((uint32_t)(Arg4));
        result = EtwWrite(Arg1, Arg2, Arg3, Arg4);
    }
    Arg1 = (*(uint64_t *)(local_rsp - 0x2F + 0x17)) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (240);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00913AF8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00913AF8[BB_00913AF8]
  bb_00913B34[BB_00913B34]
  bb_00913B4F[BB_00913B4F]
  bb_00913C2B[BB_00913C2B]
  bb_00913C48[BB_00913C48]
  bb_00913AF8 -->|branch| bb_00913C2B
  bb_00913AF8 -->|fallthrough| bb_00913B34
  bb_00913B34 -->|branch| bb_00913C2B
  bb_00913B34 -->|fallthrough| bb_00913B4F
  bb_00913B4F -->|flow| bb_00913C2B
```
