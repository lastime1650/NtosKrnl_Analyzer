# EtwTracePsIoAttribution

- RVA: `0x009F7E44`–`0x009F7F05` (길이 `193` bytes)
- VA: `0x00000001409F7E44`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A6DC4`
- 디코드: `49`개 명령, `193/193` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x009F7E8A` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (function, `0x00392450`)
- `0x009F7E9A` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x009F7EFE` → [EtwWrite](../../text/41/EtwWrite_function_0041C720.md) (function, `0x0041C720`)

### Direct callers
- [PspSetJobIoAttribution](PspSetJobIoAttribution_function_009F7C50.md) at `0x009F7CEF`

### Static image references
- `0x009F7E5E` → RVA `0x00E0A740` (`.data`; read)
- `0x009F7E6C` → RVA `0x00EFF9E8` (`.data`; read)
- `0x009F7E73` → RVA `0x000149E0` (`.rdata`; read)
- `0x009F7E7C` → RVA `0x000149D0` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x009F7E8A` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (`PAGE` → `.text`)
  - `0x009F7E9A` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x009F7EFE` → [EtwWrite](../../text/41/EtwWrite_function_0041C720.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
009F7E44  48 8B C4                        mov rax, rsp
009F7E47  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
009F7E4B  44 89 48 20                     mov dword ptr [rax + 0x20], r9d
009F7E4F  4C 89 40 18                     mov qword ptr [rax + 0x18], r8
009F7E53  89 48 08                        mov dword ptr [rax + 8], ecx
009F7E56  55                              push rbp
009F7E57  48 8B EC                        mov rbp, rsp
009F7E5A  48 83 EC 70                     sub rsp, 0x70
009F7E5E  48 8B 05 DB 28 41 00            mov rax, qword ptr [rip + 0x4128db]
009F7E65  48 33 C4                        xor rax, rsp
009F7E68  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
009F7E6C  48 8B 0D 75 7B 50 00            mov rcx, qword ptr [rip + 0x507b75]
009F7E73  48 8D 05 66 CB 61 FF            lea rax, [rip - 0x9e349a]
009F7E7A  84 D2                           test dl, dl
009F7E7C  48 8D 1D 4D CB 61 FF            lea rbx, [rip - 0x9e34b3]
009F7E83  48 0F 44 D8                     cmove rbx, rax
009F7E87  48 8B D3                        mov rdx, rbx
009F7E8A  E8 C1 A5 99 FF                  call 0x140392450
009F7E8F  84 C0                           test al, al
009F7E91  75 1B                           jne 0x1409f7eae
009F7E93  48 8B 4D F0                     mov rcx, qword ptr [rbp - 0x10]
009F7E97  48 33 CC                        xor rcx, rsp
009F7E9A  E8 A1 47 CB FF                  call 0x1406ac640
009F7E9F  48 8B 9C 24 88 00 00 00         mov rbx, qword ptr [rsp + 0x88]
009F7EA7  48 83 C4 70                     add rsp, 0x70
009F7EAB  5D                              pop rbp
009F7EAC  C3                              ret
009F7EAD  CC                              int3
009F7EAE  83 65 CC 00                     and dword ptr [rbp - 0x34], 0
009F7EB2  48 8D 45 10                     lea rax, [rbp + 0x10]
009F7EB6  83 65 DC 00                     and dword ptr [rbp - 0x24], 0
009F7EBA  B9 04 00 00 00                  mov ecx, 4
009F7EBF  83 65 EC 00                     and dword ptr [rbp - 0x14], 0
009F7EC3  45 33 C0                        xor r8d, r8d
009F7EC6  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
009F7ECA  48 8B D3                        mov rdx, rbx
009F7ECD  48 8D 45 20                     lea rax, [rbp + 0x20]
009F7ED1  89 4D C8                        mov dword ptr [rbp - 0x38], ecx
009F7ED4  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
009F7ED8  44 8D 49 FF                     lea r9d, [rcx - 1]
009F7EDC  48 8D 45 28                     lea rax, [rbp + 0x28]
009F7EE0  89 4D E8                        mov dword ptr [rbp - 0x18], ecx
009F7EE3  48 8B 0D FE 7A 50 00            mov rcx, qword ptr [rip + 0x507afe]
009F7EEA  48 89 45 E0                     mov qword ptr [rbp - 0x20], rax
009F7EEE  48 8D 45 C0                     lea rax, [rbp - 0x40]
009F7EF2  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
009F7EF7  C7 45 D8 08 00 00 00            mov dword ptr [rbp - 0x28], 8
009F7EFE  E8 1D 48 A2 FF                  call 0x14041c720
009F7F03  EB 8E                           jmp 0x1409f7e93
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EtwTracePsIoAttribution(int a1, unsigned __int8 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned int v_stack_m1C;
    unsigned int v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned int v_stack_m2C;
    unsigned int v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned int v_stack_m3C;
    unsigned int v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 16) = v_rbx;
    *(unsigned int *)(v_rsp + 32) = a4;
    *(unsigned __int64 *)(v_rsp + 24) = a3;
    *(unsigned int *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (112);
    result = (*(unsigned __int64 *)(v_rip + 4270299)) ^ (v_rsp);
    v_stack_m18 = result;
    v_rbx = v_rip - 10368179;
    if (a2 == 0) { v_rbx = v_rip - 10368154; }
    result = EtwEventEnabled(*(unsigned __int64 *)(v_rip + 5274485), v_rbx, a3, a4);
    if ((unsigned __int8)(result) != 0) goto loc_009F7EAE;
loc_009F7E93:
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, v_rbx, a3, a4);
    v_rsp = (v_rsp) + (112);
    return result;
loc_009F7EAE:
    a3 = 0;
    v_stack_m48 = v_stack_p8;
    v_stack_m40 = 4;
    v_stack_m38 = v_stack_p18;
    v_stack_m20 = 4;
    v_stack_m28 = v_stack_p20;
    v_stack_p20 = v_stack_m48;
    v_stack_m30 = 8;
    result = EtwWrite(*(unsigned __int64 *)(v_rip + 5274366), v_stack_p10, a3, 4 - 1);
    goto loc_009F7E93;
}
```

## 5. (Beta) C Style

```c
int64_t EtwTracePsIoAttribution(int32_t Arg1, uint8_t Arg2, int64_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint32_t v_stack_m1C;
    uint32_t v_stack_m20;
    uint64_t v_stack_m28;
    uint32_t v_stack_m2C;
    uint32_t v_stack_m30;
    uint64_t v_stack_m38;
    uint32_t v_stack_m3C;
    uint32_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x10) = local_rbx;
    *(uint32_t *)(local_rsp + 0x20) = Arg4;
    *(uint64_t *)(local_rsp + 0x18) = Arg3;
    *(uint32_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (112);
    result = (*(uint64_t *)(v_rip + 0x4128DB)) ^ (local_rsp);
    v_stack_m18 = result;
    local_rbx = v_rip - 10368179;
    if (Arg2 == 0) { local_rbx = v_rip - 10368154; }
    result = EtwEventEnabled(*(uint64_t *)(v_rip + 0x507B75), local_rbx, Arg3, Arg4);
    if ((uint8_t)(result) != 0) goto loc_009F7EAE;
loc_009F7E93:
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, local_rbx, Arg3, Arg4);
    local_rsp = (local_rsp) + (112);
    return result;
loc_009F7EAE:
    Arg3 = 0;
    v_stack_m48 = v_stack_p8;
    v_stack_m40 = 4;
    v_stack_m38 = v_stack_p18;
    v_stack_m20 = 4;
    v_stack_m28 = v_stack_p20;
    v_stack_p20 = v_stack_m48;
    v_stack_m30 = 8;
    result = EtwWrite(*(uint64_t *)(v_rip + 0x507AFE), v_stack_p10, Arg3, 4 - 1);
    goto loc_009F7E93;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009F7E44&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_009F7E44[BB_009F7E44]
  bb_009F7E93[BB_009F7E93]
  bb_009F7EAD[BB_009F7EAD]
  bb_009F7EAE[BB_009F7EAE]
  bb_009F7E44 -->|branch| bb_009F7EAE
  bb_009F7E44 -->|fallthrough| bb_009F7E93
  bb_009F7EAD -->|flow| bb_009F7EAE
  bb_009F7EAE -->|branch| bb_009F7E93
```
