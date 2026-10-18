# PopDiagTraceSystemIdleAction

- RVA: `0x00A31F34`–`0x00A31FEE` (길이 `186` bytes)
- VA: `0x0000000140A31F34`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000AD2BC`
- 디코드: `46`개 명령, `186/186` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x00A31F72` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (function, `0x00392450`)
- `0x00A31FCE` → [EtwWrite](../../text/41/EtwWrite_function_0041C720.md) (function, `0x0041C720`)
- `0x00A31FDA` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [PopExecuteSystemIdleAction](PopExecuteSystemIdleAction_function_00A31E7C.md) at `0x00A31EFD`

### Static image references
- `0x00A31F4A` → RVA `0x00E0A740` (`.data`; read)
- `0x00A31F58` → RVA `0x00E67858` (`.data`; read)
- `0x00A31F64` → RVA `0x00F0B408` (`.data`; read)
- `0x00A31F6B` → RVA `0x0001A2A0` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x00A31F72` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (`PAGE` → `.text`)
  - `0x00A31FCE` → [EtwWrite](../../text/41/EtwWrite_function_0041C720.md) (`PAGE` → `.text`)
  - `0x00A31FDA` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A31F34  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
00A31F39  44 89 44 24 18                  mov dword ptr [rsp + 0x18], r8d
00A31F3E  89 4C 24 08                     mov dword ptr [rsp + 8], ecx
00A31F42  55                              push rbp
00A31F43  48 8B EC                        mov rbp, rsp
00A31F46  48 83 EC 70                     sub rsp, 0x70
00A31F4A  48 8B 05 EF 87 3D 00            mov rax, qword ptr [rip + 0x3d87ef]
00A31F51  48 33 C4                        xor rax, rsp
00A31F54  48 89 45 F8                     mov qword ptr [rbp - 8], rax
00A31F58  80 3D F9 58 43 00 00            cmp byte ptr [rip + 0x4358f9], 0
00A31F5F  0F B6 DA                        movzx ebx, dl
00A31F62  74 6F                           je 0x140a31fd3
00A31F64  48 8B 0D 9D 94 4D 00            mov rcx, qword ptr [rip + 0x4d949d]
00A31F6B  48 8D 15 2E 83 5E FF            lea rdx, [rip - 0xa17cd2]
00A31F72  E8 D9 04 96 FF                  call 0x140392450
00A31F77  84 C0                           test al, al
00A31F79  74 58                           je 0x140a31fd3
00A31F7B  83 65 D4 00                     and dword ptr [rbp - 0x2c], 0
00A31F7F  48 8D 45 C0                     lea rax, [rbp - 0x40]
00A31F83  83 65 E4 00                     and dword ptr [rbp - 0x1c], 0
00A31F87  48 8D 15 12 83 5E FF            lea rdx, [rip - 0xa17cee]
00A31F8E  83 65 F4 00                     and dword ptr [rbp - 0xc], 0
00A31F92  B9 04 00 00 00                  mov ecx, 4
00A31F97  48 89 45 C8                     mov qword ptr [rbp - 0x38], rax
00A31F9B  45 33 C0                        xor r8d, r8d
00A31F9E  48 8D 45 20                     lea rax, [rbp + 0x20]
00A31FA2  89 4D D0                        mov dword ptr [rbp - 0x30], ecx
00A31FA5  48 89 45 D8                     mov qword ptr [rbp - 0x28], rax
00A31FA9  48 8D 45 10                     lea rax, [rbp + 0x10]
00A31FAD  48 89 45 E8                     mov qword ptr [rbp - 0x18], rax
00A31FB1  44 8D 49 FF                     lea r9d, [rcx - 1]
00A31FB5  48 8D 45 C8                     lea rax, [rbp - 0x38]
00A31FB9  89 4D E0                        mov dword ptr [rbp - 0x20], ecx
00A31FBC  89 4D F0                        mov dword ptr [rbp - 0x10], ecx
00A31FBF  48 8B 0D 42 94 4D 00            mov rcx, qword ptr [rip + 0x4d9442]
00A31FC6  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A31FCB  89 5D C0                        mov dword ptr [rbp - 0x40], ebx
00A31FCE  E8 4D A7 9E FF                  call 0x14041c720
00A31FD3  48 8B 4D F8                     mov rcx, qword ptr [rbp - 8]
00A31FD7  48 33 CC                        xor rcx, rsp
00A31FDA  E8 61 A6 C7 FF                  call 0x1406ac640
00A31FDF  48 8B 9C 24 88 00 00 00         mov rbx, qword ptr [rsp + 0x88]
00A31FE7  48 83 C4 70                     add rsp, 0x70
00A31FEB  5D                              pop rbp
00A31FEC  C3                              ret
00A31FED  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopDiagTraceSystemIdleAction(int a1, unsigned __int8 a2, int a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m10;
    unsigned int v_stack_m14;
    unsigned int v_stack_m18;
    unsigned __int64 v_stack_m20;
    unsigned int v_stack_m24;
    unsigned int v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned int v_stack_m34;
    unsigned int v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_p10;
    unsigned int v_stack_p18;
    unsigned int v_stack_p8;

    v_stack_p10 = v_rbx;
    v_stack_p18 = a3;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (112);
    result = (*(unsigned __int64 *)(v_rip + 4032495)) ^ (v_rsp);
    v_stack_m10 = result;
    if ((*(unsigned __int8 *)(v_rip + 4413689)) == 0) goto loc_00A31FD3;
    result = EtwEventEnabled(*(unsigned __int64 *)(v_rip + 5084317), v_rip - 10583250, a3, a4);
    if ((unsigned __int8)(result) != 0) {
        result = v_stack_m48;
        a2 = v_rip - 10583278;
        a1 = 4;
        v_stack_m40 = result;
        a3 = 0;
        result = v_stack_p18;
        v_stack_m38 = a1;
        v_stack_m30 = result;
        result = v_stack_p8;
        v_stack_m20 = result;
        a4 = a1 - 1;
        result = v_stack_m40;
        v_stack_m28 = a1;
        v_stack_m18 = a1;
        a1 = *(unsigned __int64 *)(v_rip + 5084226);
        v_stack_m58 = result;
        v_stack_m48 = a2;
        result = EtwWrite(a1, a2, a3, a4);
    }
    a1 = (v_stack_m10) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (112);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PopDiagTraceSystemIdleAction(int32_t Arg1, uint8_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m10;
    uint32_t v_stack_m14;
    uint32_t v_stack_m18;
    uint64_t v_stack_m20;
    uint32_t v_stack_m24;
    uint32_t v_stack_m28;
    uint64_t v_stack_m30;
    uint32_t v_stack_m34;
    uint32_t v_stack_m38;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m58;
    uint64_t v_stack_p10;
    uint32_t v_stack_p18;
    uint32_t v_stack_p8;

    v_stack_p10 = local_rbx;
    v_stack_p18 = Arg3;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (112);
    result = (*(uint64_t *)(v_rip + 0x3D87EF)) ^ (local_rsp);
    v_stack_m10 = result;
    if ((*(uint8_t *)(v_rip + 0x4358F9)) == 0) goto loc_00A31FD3;
    result = EtwEventEnabled(*(uint64_t *)(v_rip + 0x4D949D), v_rip - 10583250, Arg3, a4);
    if ((uint8_t)(result) != 0) {
        result = v_stack_m48;
        Arg2 = v_rip - 10583278;
        Arg1 = 4;
        v_stack_m40 = result;
        Arg3 = 0;
        result = v_stack_p18;
        v_stack_m38 = Arg1;
        v_stack_m30 = result;
        result = v_stack_p8;
        v_stack_m20 = result;
        a4 = Arg1 - 1;
        result = v_stack_m40;
        v_stack_m28 = Arg1;
        v_stack_m18 = Arg1;
        Arg1 = *(uint64_t *)(v_rip + 0x4D9442);
        v_stack_m58 = result;
        v_stack_m48 = Arg2;
        result = EtwWrite(Arg1, Arg2, Arg3, a4);
    }
    Arg1 = (v_stack_m10) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, a4);
    local_rsp = (local_rsp) + (112);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A31F34&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A31F34[BB_00A31F34]
  bb_00A31F64[BB_00A31F64]
  bb_00A31F7B[BB_00A31F7B]
  bb_00A31FD3[BB_00A31FD3]
  bb_00A31FED[BB_00A31FED]
  bb_00A31F34 -->|branch| bb_00A31FD3
  bb_00A31F34 -->|fallthrough| bb_00A31F64
  bb_00A31F64 -->|branch| bb_00A31FD3
  bb_00A31F64 -->|fallthrough| bb_00A31F7B
  bb_00A31F7B -->|flow| bb_00A31FD3
```
