# PopDiagTraceSkipTick

- RVA: `0x00762EA8`–`0x00762F57` (길이 `175` bytes)
- VA: `0x0000000140762EA8`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008B1F4`
- 디코드: `41`개 명령, `175/175` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x00762EDE` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (function, `0x00392450`)
- `0x00762F39` → [EtwWrite](../../text/41/EtwWrite_function_0041C720.md) (function, `0x0041C720`)
- `0x00762F46` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [PoInitSystem](../../init/C7/PoInitSystem_function_00C72358.md) at `0x00C72F96`

### Static image references
- `0x00762EB2` → RVA `0x00E0A740` (`.data`; read)
- `0x00762EC1` → RVA `0x00E67858` (`.data`; read)
- `0x00762ED0` → RVA `0x00F0B408` (`.data`; read)
- `0x00762ED7` → RVA `0x000231C8` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x00762EDE` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (`PAGE` → `.text`)
  - `0x00762F39` → [EtwWrite](../../text/41/EtwWrite_function_0041C720.md) (`PAGE` → `.text`)
  - `0x00762F46` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00762EA8  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00762EAD  57                              push rdi
00762EAE  48 83 EC 60                     sub rsp, 0x60
00762EB2  48 8B 05 87 78 6A 00            mov rax, qword ptr [rip + 0x6a7887]
00762EB9  48 33 C4                        xor rax, rsp
00762EBC  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
00762EC1  80 3D 90 49 70 00 00            cmp byte ptr [rip + 0x704990], 0
00762EC8  0F B6 DA                        movzx ebx, dl
00762ECB  0F B6 F9                        movzx edi, cl
00762ECE  74 6E                           je 0x140762f3e
00762ED0  48 8B 0D 31 85 7A 00            mov rcx, qword ptr [rip + 0x7a8531]
00762ED7  48 8D 15 EA 02 8C FF            lea rdx, [rip - 0x73fd16]
00762EDE  E8 6D F5 C2 FF                  call 0x140392450
00762EE3  84 C0                           test al, al
00762EE5  74 57                           je 0x140762f3e
00762EE7  83 64 24 44 00                  and dword ptr [rsp + 0x44], 0
00762EEC  48 8D 44 24 30                  lea rax, [rsp + 0x30]
00762EF1  83 64 24 54 00                  and dword ptr [rsp + 0x54], 0
00762EF6  48 8D 15 CB 02 8C FF            lea rdx, [rip - 0x73fd35]
00762EFD  B9 04 00 00 00                  mov ecx, 4
00762F02  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00762F07  48 8D 44 24 34                  lea rax, [rsp + 0x34]
00762F0C  89 4C 24 40                     mov dword ptr [rsp + 0x40], ecx
00762F10  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00762F15  45 33 C0                        xor r8d, r8d
00762F18  48 8D 44 24 38                  lea rax, [rsp + 0x38]
00762F1D  89 4C 24 50                     mov dword ptr [rsp + 0x50], ecx
00762F21  44 8D 49 FE                     lea r9d, [rcx - 2]
00762F25  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00762F2A  48 8B 0D D7 84 7A 00            mov rcx, qword ptr [rip + 0x7a84d7]
00762F31  89 7C 24 30                     mov dword ptr [rsp + 0x30], edi
00762F35  89 5C 24 34                     mov dword ptr [rsp + 0x34], ebx
00762F39  E8 E2 97 CB FF                  call 0x14041c720
00762F3E  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
00762F43  48 33 CC                        xor rcx, rsp
00762F46  E8 F5 96 F4 FF                  call 0x1406ac640
00762F4B  48 8B 5C 24 70                  mov rbx, qword ptr [rsp + 0x70]
00762F50  48 83 C4 60                     add rsp, 0x60
00762F54  5F                              pop rdi
00762F55  C3                              ret
00762F56  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopDiagTraceSkipTick(unsigned __int8 a1, unsigned __int8 a2, int a3)
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
    unsigned __int64 v_stack_m34;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (96);
    result = (*(unsigned __int64 *)(v_rip + 6977671)) ^ (v_rsp);
    v_stack_m10 = result;
    if ((*(unsigned __int8 *)(v_rip + 7358864)) == 0) goto loc_00762F3E;
    result = EtwEventEnabled(*(unsigned __int64 *)(v_rip + 8029489), v_rip - 7601430, a3, a4);
    if ((unsigned __int8)(result) != 0) {
        result = v_stack_m38;
        a2 = v_rip - 7601461;
        a1 = 4;
        v_stack_m30 = result;
        result = v_stack_m34;
        v_stack_m28 = a1;
        v_stack_m20 = result;
        a3 = 0;
        result = v_stack_m30;
        v_stack_m18 = a1;
        a4 = a1 - 2;
        v_stack_m48 = result;
        a1 = *(unsigned __int64 *)(v_rip + 8029399);
        v_stack_m38 = a1;
        v_stack_m34 = a2;
        result = EtwWrite(a1, a2, a3, a4);
    }
    a1 = (v_stack_m10) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (96);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PopDiagTraceSkipTick(uint8_t Arg1, uint8_t Arg2, int32_t Arg3)
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
    uint64_t v_stack_m34;
    uint64_t v_stack_m38;
    uint64_t v_stack_m48;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (96);
    result = (*(uint64_t *)(v_rip + 0x6A7887)) ^ (local_rsp);
    v_stack_m10 = result;
    if ((*(uint8_t *)(v_rip + 0x704990)) == 0) goto loc_00762F3E;
    result = EtwEventEnabled(*(uint64_t *)(v_rip + 0x7A8531), v_rip - 7601430, Arg3, a4);
    if ((uint8_t)(result) != 0) {
        result = v_stack_m38;
        Arg2 = v_rip - 7601461;
        Arg1 = 4;
        v_stack_m30 = result;
        result = v_stack_m34;
        v_stack_m28 = Arg1;
        v_stack_m20 = result;
        Arg3 = 0;
        result = v_stack_m30;
        v_stack_m18 = Arg1;
        a4 = Arg1 - 2;
        v_stack_m48 = result;
        Arg1 = *(uint64_t *)(v_rip + 0x7A84D7);
        v_stack_m38 = Arg1;
        v_stack_m34 = Arg2;
        result = EtwWrite(Arg1, Arg2, Arg3, a4);
    }
    Arg1 = (v_stack_m10) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, a4);
    local_rsp = (local_rsp) + (96);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00762EA8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00762EA8[BB_00762EA8]
  bb_00762ED0[BB_00762ED0]
  bb_00762EE7[BB_00762EE7]
  bb_00762F3E[BB_00762F3E]
  bb_00762F56[BB_00762F56]
  bb_00762EA8 -->|branch| bb_00762F3E
  bb_00762EA8 -->|fallthrough| bb_00762ED0
  bb_00762ED0 -->|branch| bb_00762F3E
  bb_00762ED0 -->|fallthrough| bb_00762EE7
  bb_00762EE7 -->|flow| bb_00762F3E
```
