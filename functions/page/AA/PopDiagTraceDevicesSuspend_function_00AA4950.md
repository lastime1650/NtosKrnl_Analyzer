# PopDiagTraceDevicesSuspend

- RVA: `0x00AA4950`–`0x00AA4A0A` (길이 `186` bytes)
- VA: `0x0000000140AA4950`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BB560`
- 디코드: `46`개 명령, `186/186` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x00AA498E` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (function, `0x00392450`)
- `0x00AA49EA` → [EtwWrite](../../text/41/EtwWrite_function_0041C720.md) (function, `0x0041C720`)
- `0x00AA49F6` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [PoBroadcastSystemState](../../pagelk/B7/PoBroadcastSystemState_function_00B761B0.md) at `0x00B764B2`

### Static image references
- `0x00AA4966` → RVA `0x00E0A740` (`.data`; read)
- `0x00AA4974` → RVA `0x00E67858` (`.data`; read)
- `0x00AA4980` → RVA `0x00F0B408` (`.data`; read)
- `0x00AA4987` → RVA `0x0001C830` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x00AA498E` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (`PAGE` → `.text`)
  - `0x00AA49EA` → [EtwWrite](../../text/41/EtwWrite_function_0041C720.md) (`PAGE` → `.text`)
  - `0x00AA49F6` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00AA4950  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00AA4955  44 89 44 24 18                  mov dword ptr [rsp + 0x18], r8d
00AA495A  89 54 24 10                     mov dword ptr [rsp + 0x10], edx
00AA495E  55                              push rbp
00AA495F  48 8B EC                        mov rbp, rsp
00AA4962  48 83 EC 70                     sub rsp, 0x70
00AA4966  48 8B 05 D3 5D 36 00            mov rax, qword ptr [rip + 0x365dd3]
00AA496D  48 33 C4                        xor rax, rsp
00AA4970  48 89 45 F8                     mov qword ptr [rbp - 8], rax
00AA4974  80 3D DD 2E 3C 00 00            cmp byte ptr [rip + 0x3c2edd], 0
00AA497B  0F B6 D9                        movzx ebx, cl
00AA497E  74 6F                           je 0x140aa49ef
00AA4980  48 8B 0D 81 6A 46 00            mov rcx, qword ptr [rip + 0x466a81]
00AA4987  48 8D 15 A2 7E 57 FF            lea rdx, [rip - 0xa8815e]
00AA498E  E8 BD DA 8E FF                  call 0x140392450
00AA4993  84 C0                           test al, al
00AA4995  74 58                           je 0x140aa49ef
00AA4997  83 65 D4 00                     and dword ptr [rbp - 0x2c], 0
00AA499B  48 8D 45 C0                     lea rax, [rbp - 0x40]
00AA499F  83 65 E4 00                     and dword ptr [rbp - 0x1c], 0
00AA49A3  48 8D 15 86 7E 57 FF            lea rdx, [rip - 0xa8817a]
00AA49AA  83 65 F4 00                     and dword ptr [rbp - 0xc], 0
00AA49AE  B9 04 00 00 00                  mov ecx, 4
00AA49B3  48 89 45 C8                     mov qword ptr [rbp - 0x38], rax
00AA49B7  45 33 C0                        xor r8d, r8d
00AA49BA  48 8D 45 18                     lea rax, [rbp + 0x18]
00AA49BE  89 4D D0                        mov dword ptr [rbp - 0x30], ecx
00AA49C1  48 89 45 D8                     mov qword ptr [rbp - 0x28], rax
00AA49C5  48 8D 45 20                     lea rax, [rbp + 0x20]
00AA49C9  48 89 45 E8                     mov qword ptr [rbp - 0x18], rax
00AA49CD  44 8D 49 FF                     lea r9d, [rcx - 1]
00AA49D1  48 8D 45 C8                     lea rax, [rbp - 0x38]
00AA49D5  89 4D E0                        mov dword ptr [rbp - 0x20], ecx
00AA49D8  89 4D F0                        mov dword ptr [rbp - 0x10], ecx
00AA49DB  48 8B 0D 26 6A 46 00            mov rcx, qword ptr [rip + 0x466a26]
00AA49E2  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AA49E7  89 5D C0                        mov dword ptr [rbp - 0x40], ebx
00AA49EA  E8 31 7D 97 FF                  call 0x14041c720
00AA49EF  48 8B 4D F8                     mov rcx, qword ptr [rbp - 8]
00AA49F3  48 33 CC                        xor rcx, rsp
00AA49F6  E8 45 7C C0 FF                  call 0x1406ac640
00AA49FB  48 8B 9C 24 80 00 00 00         mov rbx, qword ptr [rsp + 0x80]
00AA4A03  48 83 C4 70                     add rsp, 0x70
00AA4A07  5D                              pop rbp
00AA4A08  C3                              ret
00AA4A09  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopDiagTraceDevicesSuspend(unsigned __int8 a1, int a2, int a3)
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
    unsigned int v_stack_p10;
    unsigned int v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p18 = a3;
    v_stack_p10 = a2;
    v_rsp = (v_rsp) - (112);
    result = (*(unsigned __int64 *)(v_rip + 3562963)) ^ (v_rsp);
    v_stack_m10 = result;
    if ((*(unsigned __int8 *)(v_rip + 3944157)) == 0) goto loc_00AA49EF;
    result = EtwEventEnabled(*(unsigned __int64 *)(v_rip + 4614785), v_rip - 11043166, a3, a4);
    if ((unsigned __int8)(result) != 0) {
        result = v_stack_m48;
        a2 = v_rip - 11043194;
        a1 = 4;
        v_stack_m40 = result;
        a3 = 0;
        result = v_stack_p10;
        v_stack_m38 = a1;
        v_stack_m30 = result;
        result = v_stack_p18;
        v_stack_m20 = result;
        a4 = a1 - 1;
        result = v_stack_m40;
        v_stack_m28 = a1;
        v_stack_m18 = a1;
        a1 = *(unsigned __int64 *)(v_rip + 4614694);
        v_stack_m58 = result;
        v_stack_m48 = a1;
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
int64_t PopDiagTraceDevicesSuspend(uint8_t Arg1, int32_t Arg2, int32_t Arg3)
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
    uint32_t v_stack_p10;
    uint32_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p18 = Arg3;
    v_stack_p10 = Arg2;
    local_rsp = (local_rsp) - (112);
    result = (*(uint64_t *)(v_rip + 0x365DD3)) ^ (local_rsp);
    v_stack_m10 = result;
    if ((*(uint8_t *)(v_rip + 0x3C2EDD)) == 0) goto loc_00AA49EF;
    result = EtwEventEnabled(*(uint64_t *)(v_rip + 0x466A81), v_rip - 11043166, Arg3, a4);
    if ((uint8_t)(result) != 0) {
        result = v_stack_m48;
        Arg2 = v_rip - 11043194;
        Arg1 = 4;
        v_stack_m40 = result;
        Arg3 = 0;
        result = v_stack_p10;
        v_stack_m38 = Arg1;
        v_stack_m30 = result;
        result = v_stack_p18;
        v_stack_m20 = result;
        a4 = Arg1 - 1;
        result = v_stack_m40;
        v_stack_m28 = Arg1;
        v_stack_m18 = Arg1;
        Arg1 = *(uint64_t *)(v_rip + 0x466A26);
        v_stack_m58 = result;
        v_stack_m48 = Arg1;
        result = EtwWrite(Arg1, Arg2, Arg3, a4);
    }
    Arg1 = (v_stack_m10) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, a4);
    local_rsp = (local_rsp) + (112);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00AA4950&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00AA4950[BB_00AA4950]
  bb_00AA4980[BB_00AA4980]
  bb_00AA4997[BB_00AA4997]
  bb_00AA49EF[BB_00AA49EF]
  bb_00AA4A09[BB_00AA4A09]
  bb_00AA4950 -->|branch| bb_00AA49EF
  bb_00AA4950 -->|fallthrough| bb_00AA4980
  bb_00AA4980 -->|branch| bb_00AA49EF
  bb_00AA4980 -->|fallthrough| bb_00AA4997
  bb_00AA4997 -->|flow| bb_00AA49EF
```
