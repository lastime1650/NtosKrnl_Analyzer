# CmpTraceHiveUnloadStop

- RVA: `0x009B38B8`–`0x009B3941` (길이 `137` bytes)
- VA: `0x00000001409B38B8`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006CABC`
- 디코드: `30`개 명령, `137/137` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x009B38E8` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (function, `0x00392450`)
- `0x009B38F9` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x009B393A` → [EtwWrite](../../text/41/EtwWrite_function_0041C720.md) (function, `0x0041C720`)

### Direct callers
- [CmpCompleteUnloadKey](CmpCompleteUnloadKey_function_009B32FC.md) at `0x009B34E9`

### Static image references
- `0x009B38C0` → RVA `0x00E0A740` (`.data`; read)
- `0x009B38CF` → RVA `0x00013C50` (`.rdata`; read)
- `0x009B38D6` → RVA `0x00FD8018` (`PAGEDATA`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x009B38E8` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (`PAGE` → `.text`)
  - `0x009B38F9` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x009B393A` → [EtwWrite](../../text/41/EtwWrite_function_0041C720.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
009B38B8  89 4C 24 08                     mov dword ptr [rsp + 8], ecx
009B38BC  48 83 EC 68                     sub rsp, 0x68
009B38C0  48 8B 05 79 6E 45 00            mov rax, qword ptr [rip + 0x456e79]
009B38C7  48 33 C4                        xor rax, rsp
009B38CA  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
009B38CF  0F 10 05 7A 03 66 FF            movups xmm0, xmmword ptr [rip - 0x99fc86]
009B38D6  48 8B 0D 3B 47 62 00            mov rcx, qword ptr [rip + 0x62473b]
009B38DD  48 8D 54 24 30                  lea rdx, [rsp + 0x30]
009B38E2  F3 0F 7F 44 24 30               movdqu xmmword ptr [rsp + 0x30], xmm0
009B38E8  E8 63 EB 9D FF                  call 0x140392450
009B38ED  84 C0                           test al, al
009B38EF  75 13                           jne 0x1409b3904
009B38F1  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
009B38F6  48 33 CC                        xor rcx, rsp
009B38F9  E8 42 8D CF FF                  call 0x1406ac640
009B38FE  48 83 C4 68                     add rsp, 0x68
009B3902  C3                              ret
009B3903  CC                              int3
009B3904  83 64 24 4C 00                  and dword ptr [rsp + 0x4c], 0
009B3909  48 8D 44 24 70                  lea rax, [rsp + 0x70]
009B390E  48 8B 0D 03 47 62 00            mov rcx, qword ptr [rip + 0x624703]
009B3915  48 8D 54 24 30                  lea rdx, [rsp + 0x30]
009B391A  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
009B391F  41 B9 01 00 00 00               mov r9d, 1
009B3925  48 8D 44 24 40                  lea rax, [rsp + 0x40]
009B392A  C7 44 24 48 04 00 00 00         mov dword ptr [rsp + 0x48], 4
009B3932  45 33 C0                        xor r8d, r8d
009B3935  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
009B393A  E8 E1 8D A6 FF                  call 0x14041c720
009B393F  EB B0                           jmp 0x1409b38f1
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpTraceHiveUnloadStop(int a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p40;
    unsigned int v_stack_p48;
    unsigned int v_stack_p4C;
    unsigned __int64 v_stack_p70;
    unsigned int v_stack_p8;

    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (104);
    result = (*(unsigned __int64 *)(v_rip + 4550265)) ^ (v_rsp);
    v_stack_m18 = result;
    v_stack_m38 = v_xmm0;
    result = EtwEventEnabled(*(unsigned __int64 *)(v_rip + 6440763), v_stack_m38, a3, a4);
    if ((unsigned __int8)(result) != 0) goto loc_009B3904;
loc_009B38F1:
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, v_stack_m38, a3, a4);
    v_rsp = (v_rsp) + (104);
    return result;
loc_009B3904:
    v_stack_p40 = v_stack_p70;
    v_stack_p48 = 4;
    a3 = 0;
    v_stack_p20 = v_stack_p40;
    result = EtwWrite(*(unsigned __int64 *)(v_rip + 6440707), v_stack_p30, a3, 1);
    goto loc_009B38F1;
}
```

## 5. (Beta) C Style

```c
int64_t CmpTraceHiveUnloadStop(int32_t Arg1, int64_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_m38;
    uint64_t v_stack_p20;
    uint64_t v_stack_p30;
    uint64_t v_stack_p40;
    uint32_t v_stack_p48;
    uint32_t v_stack_p4C;
    uint64_t v_stack_p70;
    uint32_t v_stack_p8;

    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (104);
    result = (*(uint64_t *)(v_rip + 0x456E79)) ^ (local_rsp);
    v_stack_m18 = result;
    v_stack_m38 = v_xmm0;
    result = EtwEventEnabled(*(uint64_t *)(v_rip + 0x62473B), v_stack_m38, Arg3, a4);
    if ((uint8_t)(result) != 0) goto loc_009B3904;
loc_009B38F1:
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, v_stack_m38, Arg3, a4);
    local_rsp = (local_rsp) + (104);
    return result;
loc_009B3904:
    v_stack_p40 = v_stack_p70;
    v_stack_p48 = 4;
    Arg3 = 0;
    v_stack_p20 = v_stack_p40;
    result = EtwWrite(*(uint64_t *)(v_rip + 0x624703), v_stack_p30, Arg3, 1);
    goto loc_009B38F1;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009B38B8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_009B38B8[BB_009B38B8]
  bb_009B38F1[BB_009B38F1]
  bb_009B3903[BB_009B3903]
  bb_009B3904[BB_009B3904]
  bb_009B38B8 -->|branch| bb_009B3904
  bb_009B38B8 -->|fallthrough| bb_009B38F1
  bb_009B3903 -->|flow| bb_009B3904
  bb_009B3904 -->|branch| bb_009B38F1
```
