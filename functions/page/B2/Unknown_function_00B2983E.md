# sub_00B2983E

- RVA: `0x00B2983E`–`0x00B29933` (길이 `245` bytes)
- VA: `0x0000000140B2983E`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000964A4`
- 디코드: `40`개 명령, `245/245` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00B29922` → [SepAdtOpenObjectAuditAlarm](../91/SepAdtOpenObjectAuditAlarm_function_0091F23C.md) (function, `0x0091F23C`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **3**
  - `0x00B29842` → [NtOpenObjectAuditAlarm + 0x636](../97/NtOpenObjectAuditAlarm_function_00974700.md) (`tail-transfer`)
  - `0x00B2984B` → [NtOpenObjectAuditAlarm + 0x642](../97/NtOpenObjectAuditAlarm_function_00974700.md) (`tail-transfer`)
  - `0x00B2992E` → [NtOpenObjectAuditAlarm + 0x3FD](../97/NtOpenObjectAuditAlarm_function_00974700.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00B2983E  48 8B 57 18                     mov rdx, qword ptr [rdi + 0x18]
00B29842  E9 EF B4 E4 FF                  jmp 0x140974d36
00B29847  48 8B 4F 18                     mov rcx, qword ptr [rdi + 0x18]
00B2984B  E9 F2 B4 E4 FF                  jmp 0x140974d42
00B29850  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00B29859  48 8B 80 B8 00 00 00            mov rax, qword ptr [rax + 0xb8]
00B29860  48 F7 9C 24 E0 00 00 00         neg qword ptr [rsp + 0xe0]
00B29868  4D 1B C0                        sbb r8, r8
00B2986B  48 8D 8C 24 F0 00 00 00         lea rcx, [rsp + 0xf0]
00B29873  4C 23 C1                        and r8, rcx
00B29876  48 89 9C 24 90 00 00 00         mov qword ptr [rsp + 0x90], rbx
00B2987E  48 89 9C 24 88 00 00 00         mov qword ptr [rsp + 0x88], rbx
00B29886  48 89 9C 24 80 00 00 00         mov qword ptr [rsp + 0x80], rbx
00B2988E  89 5C 24 78                     mov dword ptr [rsp + 0x78], ebx
00B29892  48 89 5C 24 70                  mov qword ptr [rsp + 0x70], rbx
00B29897  C7 44 24 68 02 00 00 00         mov dword ptr [rsp + 0x68], 2
00B2989F  48 8B 80 D0 01 00 00            mov rax, qword ptr [rax + 0x1d0]
00B298A6  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
00B298AB  44 88 7C 24 58                  mov byte ptr [rsp + 0x58], r15b
00B298B0  48 8B 84 24 D8 00 00 00         mov rax, qword ptr [rsp + 0xd8]
00B298B8  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
00B298BD  8B 84 24 98 01 00 00            mov eax, dword ptr [rsp + 0x198]
00B298C4  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
00B298C8  8B 84 24 90 01 00 00            mov eax, dword ptr [rsp + 0x190]
00B298CF  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
00B298D3  48 8B 84 24 08 01 00 00         mov rax, qword ptr [rsp + 0x108]
00B298DB  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00B298E0  48 8B 84 24 B8 00 00 00         mov rax, qword ptr [rsp + 0xb8]
00B298E8  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00B298ED  48 8B BC 24 B0 00 00 00         mov rdi, qword ptr [rsp + 0xb0]
00B298F5  48 89 7C 24 28                  mov qword ptr [rsp + 0x28], rdi
00B298FA  48 8B 84 24 D0 00 00 00         mov rax, qword ptr [rsp + 0xd0]
00B29902  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00B29907  48 8B B4 24 C0 00 00 00         mov rsi, qword ptr [rsp + 0xc0]
00B2990F  4C 8B CE                        mov r9, rsi
00B29912  48 8B 94 24 C8 00 00 00         mov rdx, qword ptr [rsp + 0xc8]
00B2991A  0F B7 8C 24 AC 00 00 00         movzx ecx, word ptr [rsp + 0xac]
00B29922  E8 15 59 DF FF                  call 0x14091f23c
00B29927  88 84 24 A0 00 00 00            mov byte ptr [rsp + 0xa0], al
00B2992E  E9 CA B1 E4 FF                  jmp 0x140974afd
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00B2983E(__int64 a1, __int64 a2, __int64 a3)
{
    unsigned __int64 v_stack_p108;
    unsigned int v_stack_p190;
    unsigned int v_stack_p198;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned int v_stack_p40;
    unsigned int v_stack_p48;
    unsigned __int64 v_stack_p50;
    unsigned __int8 v_stack_p58;
    unsigned __int64 v_stack_p60;
    unsigned int v_stack_p68;
    unsigned __int64 v_stack_p70;
    unsigned int v_stack_p78;
    unsigned __int64 v_stack_p80;
    unsigned __int64 v_stack_p88;
    unsigned __int64 v_stack_p90;
    unsigned __int8 v_stack_pA0;
    unsigned __int16 v_stack_pAC;
    unsigned __int64 v_stack_pB0;
    unsigned __int64 v_stack_pB8;
    unsigned __int64 v_stack_pC0;
    unsigned __int64 v_stack_pC8;
    unsigned __int64 v_stack_pD0;
    unsigned __int64 v_stack_pD8;
    unsigned __int64 v_stack_pE0;
    unsigned __int64 v_stack_pF0;
}
```

## 5. (Beta) C Style

```c
int64_t sub_00B2983E(int64_t Arg1, int64_t Arg2, int64_t Arg3)
{
    uint64_t v_stack_p108;
    uint32_t v_stack_p190;
    uint32_t v_stack_p198;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p30;
    uint64_t v_stack_p38;
    uint32_t v_stack_p40;
    uint32_t v_stack_p48;
    uint64_t v_stack_p50;
    uint8_t v_stack_p58;
    uint64_t v_stack_p60;
    uint32_t v_stack_p68;
    uint64_t v_stack_p70;
    uint32_t v_stack_p78;
    uint64_t v_stack_p80;
    uint64_t v_stack_p88;
    uint64_t v_stack_p90;
    uint8_t v_stack_pA0;
    uint16_t v_stack_pAC;
    uint64_t v_stack_pB0;
    uint64_t v_stack_pB8;
    uint64_t v_stack_pC0;
    uint64_t v_stack_pC8;
    uint64_t v_stack_pD0;
    uint64_t v_stack_pD8;
    uint64_t v_stack_pE0;
    uint64_t v_stack_pF0;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00B2983E&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B2983E[BB_00B2983E]
  bb_00B29847[BB_00B29847]
  bb_00B29850[BB_00B29850]
```
