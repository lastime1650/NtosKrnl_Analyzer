# PopDiagTraceSystemIdleAssessment

- RVA: `0x00A31FF4`–`0x00A320AE` (길이 `186` bytes)
- VA: `0x0000000140A31FF4`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000AD2D4`
- 디코드: `46`개 명령, `186/186` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x00A32032` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (function, `0x00392450`)
- `0x00A3208E` → [EtwWrite](../../text/41/EtwWrite_function_0041C720.md) (function, `0x0041C720`)
- `0x00A3209A` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [PopIsSystemIdle](PopIsSystemIdle_function_00A31BD8.md) at `0x00A31C7B`

### Static image references
- `0x00A32009` → RVA `0x00E0A740` (`.data`; read)
- `0x00A32017` → RVA `0x00E67858` (`.data`; read)
- `0x00A32024` → RVA `0x00F0B408` (`.data`; read)
- `0x00A3202B` → RVA `0x0001A290` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x00A32032` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (`PAGE` → `.text`)
  - `0x00A3208E` → [EtwWrite](../../text/41/EtwWrite_function_0041C720.md) (`PAGE` → `.text`)
  - `0x00A3209A` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A31FF4  48 89 5C 24 18                  mov qword ptr [rsp + 0x18], rbx
00A31FF9  89 54 24 10                     mov dword ptr [rsp + 0x10], edx
00A31FFD  89 4C 24 08                     mov dword ptr [rsp + 8], ecx
00A32001  55                              push rbp
00A32002  48 8B EC                        mov rbp, rsp
00A32005  48 83 EC 70                     sub rsp, 0x70
00A32009  48 8B 05 30 87 3D 00            mov rax, qword ptr [rip + 0x3d8730]
00A32010  48 33 C4                        xor rax, rsp
00A32013  48 89 45 F8                     mov qword ptr [rbp - 8], rax
00A32017  80 3D 3A 58 43 00 00            cmp byte ptr [rip + 0x43583a], 0
00A3201E  41 0F B6 D8                     movzx ebx, r8b
00A32022  74 6F                           je 0x140a32093
00A32024  48 8B 0D DD 93 4D 00            mov rcx, qword ptr [rip + 0x4d93dd]
00A3202B  48 8D 15 5E 82 5E FF            lea rdx, [rip - 0xa17da2]
00A32032  E8 19 04 96 FF                  call 0x140392450
00A32037  84 C0                           test al, al
00A32039  74 58                           je 0x140a32093
00A3203B  83 65 D4 00                     and dword ptr [rbp - 0x2c], 0
00A3203F  48 8D 45 10                     lea rax, [rbp + 0x10]
00A32043  83 65 E4 00                     and dword ptr [rbp - 0x1c], 0
00A32047  48 8D 15 42 82 5E FF            lea rdx, [rip - 0xa17dbe]
00A3204E  83 65 F4 00                     and dword ptr [rbp - 0xc], 0
00A32052  B9 04 00 00 00                  mov ecx, 4
00A32057  48 89 45 C8                     mov qword ptr [rbp - 0x38], rax
00A3205B  45 33 C0                        xor r8d, r8d
00A3205E  48 8D 45 18                     lea rax, [rbp + 0x18]
00A32062  89 4D D0                        mov dword ptr [rbp - 0x30], ecx
00A32065  48 89 45 D8                     mov qword ptr [rbp - 0x28], rax
00A32069  48 8D 45 C0                     lea rax, [rbp - 0x40]
00A3206D  48 89 45 E8                     mov qword ptr [rbp - 0x18], rax
00A32071  44 8D 49 FF                     lea r9d, [rcx - 1]
00A32075  48 8D 45 C8                     lea rax, [rbp - 0x38]
00A32079  89 4D E0                        mov dword ptr [rbp - 0x20], ecx
00A3207C  89 4D F0                        mov dword ptr [rbp - 0x10], ecx
00A3207F  48 8B 0D 82 93 4D 00            mov rcx, qword ptr [rip + 0x4d9382]
00A32086  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A3208B  89 5D C0                        mov dword ptr [rbp - 0x40], ebx
00A3208E  E8 8D A6 9E FF                  call 0x14041c720
00A32093  48 8B 4D F8                     mov rcx, qword ptr [rbp - 8]
00A32097  48 33 CC                        xor rcx, rsp
00A3209A  E8 A1 A5 C7 FF                  call 0x1406ac640
00A3209F  48 8B 9C 24 90 00 00 00         mov rbx, qword ptr [rsp + 0x90]
00A320A7  48 83 C4 70                     add rsp, 0x70
00A320AB  5D                              pop rbp
00A320AC  C3                              ret
00A320AD  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopDiagTraceSystemIdleAssessment(int a1, int a2, int a3)
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
    unsigned __int64 v_stack_p18;
    unsigned int v_stack_p8;

    v_stack_p18 = v_rbx;
    v_stack_p10 = a2;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (112);
    result = (*(unsigned __int64 *)(v_rip + 4032304)) ^ (v_rsp);
    v_stack_m10 = result;
    if ((*(unsigned __int8 *)(v_rip + 4413498)) == 0) goto loc_00A32093;
    result = EtwEventEnabled(*(unsigned __int64 *)(v_rip + 5084125), v_rip - 10583458, a3, a4);
    if ((unsigned __int8)(result) != 0) {
        result = v_stack_p8;
        a2 = v_rip - 10583486;
        a1 = 4;
        v_stack_m40 = result;
        a3 = 0;
        result = v_stack_p10;
        v_stack_m38 = a1;
        v_stack_m30 = result;
        result = v_stack_m48;
        v_stack_m20 = result;
        a4 = a1 - 1;
        result = v_stack_m40;
        v_stack_m28 = a1;
        v_stack_m18 = a1;
        a1 = *(unsigned __int64 *)(v_rip + 5084034);
        v_stack_m58 = result;
        v_stack_m48 = (unsigned int)((unsigned __int8)(a3));
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
int64_t PopDiagTraceSystemIdleAssessment(int32_t Arg1, int32_t Arg2, int32_t Arg3)
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
    uint64_t v_stack_p18;
    uint32_t v_stack_p8;

    v_stack_p18 = local_rbx;
    v_stack_p10 = Arg2;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (112);
    result = (*(uint64_t *)(v_rip + 0x3D8730)) ^ (local_rsp);
    v_stack_m10 = result;
    if ((*(uint8_t *)(v_rip + 0x43583A)) == 0) goto loc_00A32093;
    result = EtwEventEnabled(*(uint64_t *)(v_rip + 0x4D93DD), v_rip - 10583458, Arg3, a4);
    if ((uint8_t)(result) != 0) {
        result = v_stack_p8;
        Arg2 = v_rip - 10583486;
        Arg1 = 4;
        v_stack_m40 = result;
        Arg3 = 0;
        result = v_stack_p10;
        v_stack_m38 = Arg1;
        v_stack_m30 = result;
        result = v_stack_m48;
        v_stack_m20 = result;
        a4 = Arg1 - 1;
        result = v_stack_m40;
        v_stack_m28 = Arg1;
        v_stack_m18 = Arg1;
        Arg1 = *(uint64_t *)(v_rip + 0x4D9382);
        v_stack_m58 = result;
        v_stack_m48 = (uint32_t)((uint8_t)(Arg3));
        result = EtwWrite(Arg1, Arg2, Arg3, a4);
    }
    Arg1 = (v_stack_m10) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, a4);
    local_rsp = (local_rsp) + (112);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A31FF4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A31FF4[BB_00A31FF4]
  bb_00A32024[BB_00A32024]
  bb_00A3203B[BB_00A3203B]
  bb_00A32093[BB_00A32093]
  bb_00A320AD[BB_00A320AD]
  bb_00A31FF4 -->|branch| bb_00A32093
  bb_00A31FF4 -->|fallthrough| bb_00A32024
  bb_00A32024 -->|branch| bb_00A32093
  bb_00A32024 -->|fallthrough| bb_00A3203B
  bb_00A3203B -->|flow| bb_00A32093
```
