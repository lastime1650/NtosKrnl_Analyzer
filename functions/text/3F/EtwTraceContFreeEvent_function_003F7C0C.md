# EtwTraceContFreeEvent

- RVA: `0x003F7C0C`–`0x003F7CB4` (길이 `168` bytes)
- VA: `0x00000001403F7C0C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00098260`
- 디코드: `38`개 명령, `168/168` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x003F7C39` → [EtwEventEnabled](../39/EtwEventEnabled_function_00392450.md) (function, `0x00392450`)
- `0x003F7C4C` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x003F7CAD` → [EtwWriteEx](../25/EtwWriteEx_function_0025F0D0.md) (function, `0x0025F0D0`)

### Direct callers
- [MmFreeContiguousMemory](MmFreeContiguousMemory_function_003F6F60.md) at `0x003F7085`
- [MmFreeContiguousMemory](MmFreeContiguousMemory_function_003F6F60.md) at `0x003F70F2`

### Static image references
- `0x003F7C16` → RVA `0x00E0A740` (`.data`; read)
- `0x003F7C2B` → RVA `0x00EFF848` (`.data`; read)
- `0x003F7C32` → RVA `0x00013088` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003F7C0C  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
003F7C11  57                              push rdi
003F7C12  48 83 EC 70                     sub rsp, 0x70
003F7C16  48 8B 05 23 2B A1 00            mov rax, qword ptr [rip + 0xa12b23]
003F7C1D  48 33 C4                        xor rax, rsp
003F7C20  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
003F7C25  48 8B DA                        mov rbx, rdx
003F7C28  48 8B F9                        mov rdi, rcx
003F7C2B  48 8B 0D 16 7C B0 00            mov rcx, qword ptr [rip + 0xb07c16]
003F7C32  48 8D 15 4F B4 C1 FF            lea rdx, [rip - 0x3e4bb1]
003F7C39  E8 12 A8 F9 FF                  call 0x140392450
003F7C3E  33 C9                           xor ecx, ecx
003F7C40  84 C0                           test al, al
003F7C42  75 1C                           jne 0x1403f7c60
003F7C44  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
003F7C49  48 33 CC                        xor rcx, rsp
003F7C4C  E8 EF 49 2B 00                  call 0x1406ac640
003F7C51  48 8B 9C 24 80 00 00 00         mov rbx, qword ptr [rsp + 0x80]
003F7C59  48 83 C4 70                     add rsp, 0x70
003F7C5D  5F                              pop rdi
003F7C5E  C3                              ret
003F7C5F  CC                              int3
003F7C60  48 8D 44 24 40                  lea rax, [rsp + 0x40]
003F7C65  48 89 7C 24 40                  mov qword ptr [rsp + 0x40], rdi
003F7C6A  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
003F7C6F  48 8D 15 12 B4 C1 FF            lea rdx, [rip - 0x3e4bee]
003F7C76  48 8D 44 24 50                  lea rax, [rsp + 0x50]
003F7C7B  48 89 5C 24 48                  mov qword ptr [rsp + 0x48], rbx
003F7C80  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
003F7C85  41 B9 01 00 00 00               mov r9d, 1
003F7C8B  44 89 4C 24 30                  mov dword ptr [rsp + 0x30], r9d
003F7C90  45 33 C0                        xor r8d, r8d
003F7C93  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
003F7C98  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
003F7C9D  48 8B 0D A4 7B B0 00            mov rcx, qword ptr [rip + 0xb07ba4]
003F7CA4  48 C7 44 24 58 10 00 00 00      mov qword ptr [rsp + 0x58], 0x10
003F7CAD  E8 1E 74 E6 FF                  call 0x14025f0d0
003F7CB2  EB 90                           jmp 0x1403f7c44
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EtwTraceContFreeEvent(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned int v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (112);
    result = (*(unsigned __int64 *)(v_rip + 10562339)) ^ (v_rsp);
    v_stack_m18 = result;
    result = EtwEventEnabled(*(unsigned __int64 *)(v_rip + 11566102), v_rip - 4082609, a3, a4);
    a1 = 0;
    if ((unsigned __int8)(result) != 0) goto loc_003F7C60;
loc_003F7C44:
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, v_rip - 4082609, a3, a4);
    v_rsp = (v_rsp) + (112);
    return result;
loc_003F7C60:
    v_stack_p40 = a1;
    v_stack_p50 = v_stack_p40;
    v_stack_p48 = v_stack_p8;
    v_stack_p38 = v_stack_p50;
    v_stack_p30 = 1;
    a3 = 0;
    v_stack_p28 = a1;
    v_stack_p20 = a1;
    v_stack_p58 = 16;
    result = EtwWriteEx(*(unsigned __int64 *)(v_rip + 11565988), v_rip - 4082670, a3, 1);
    goto loc_003F7C44;
}
```

## 5. (Beta) C Style

```c
int64_t EtwTraceContFreeEvent(int64_t Arg1, int64_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint32_t v_stack_p30;
    uint64_t v_stack_p38;
    uint64_t v_stack_p40;
    uint64_t v_stack_p48;
    uint64_t v_stack_p50;
    uint64_t v_stack_p58;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (112);
    result = (*(uint64_t *)(v_rip + 0xA12B23)) ^ (local_rsp);
    v_stack_m18 = result;
    result = EtwEventEnabled(*(uint64_t *)(v_rip + 0xB07C16), v_rip - 4082609, Arg3, a4);
    Arg1 = 0;
    if ((uint8_t)(result) != 0) goto loc_003F7C60;
loc_003F7C44:
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, v_rip - 4082609, Arg3, a4);
    local_rsp = (local_rsp) + (112);
    return result;
loc_003F7C60:
    v_stack_p40 = Arg1;
    v_stack_p50 = v_stack_p40;
    v_stack_p48 = v_stack_p8;
    v_stack_p38 = v_stack_p50;
    v_stack_p30 = 1;
    Arg3 = 0;
    v_stack_p28 = Arg1;
    v_stack_p20 = Arg1;
    v_stack_p58 = 16;
    result = EtwWriteEx(*(uint64_t *)(v_rip + 0xB07BA4), v_rip - 4082670, Arg3, 1);
    goto loc_003F7C44;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003F7C0C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003F7C0C[BB_003F7C0C]
  bb_003F7C44[BB_003F7C44]
  bb_003F7C5F[BB_003F7C5F]
  bb_003F7C60[BB_003F7C60]
  bb_003F7C0C -->|branch| bb_003F7C60
  bb_003F7C0C -->|fallthrough| bb_003F7C44
  bb_003F7C5F -->|flow| bb_003F7C60
  bb_003F7C60 -->|branch| bb_003F7C44
```
