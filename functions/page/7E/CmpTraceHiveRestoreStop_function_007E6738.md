# CmpTraceHiveRestoreStop

- RVA: `0x007E6738`–`0x007E67BF` (길이 `135` bytes)
- VA: `0x00000001407E6738`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00073440`
- 디코드: `29`개 명령, `135/135` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x007E6768` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (function, `0x00392450`)
- `0x007E67A7` → [EtwWrite](../../text/41/EtwWrite_function_0041C720.md) (function, `0x0041C720`)
- `0x007E67B4` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [CmRestoreKey](../7D/CmRestoreKey_function_007DCF04.md) at `0x007DDBA4`

### Static image references
- `0x007E6740` → RVA `0x00E0A740` (`.data`; read)
- `0x007E674F` → RVA `0x000234C0` (`.rdata`; read)
- `0x007E6756` → RVA `0x00FD8018` (`PAGEDATA`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x007E6768` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (`PAGE` → `.text`)
  - `0x007E67A7` → [EtwWrite](../../text/41/EtwWrite_function_0041C720.md) (`PAGE` → `.text`)
  - `0x007E67B4` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007E6738  89 4C 24 08                     mov dword ptr [rsp + 8], ecx
007E673C  48 83 EC 68                     sub rsp, 0x68
007E6740  48 8B 05 F9 3F 62 00            mov rax, qword ptr [rip + 0x623ff9]
007E6747  48 33 C4                        xor rax, rsp
007E674A  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
007E674F  0F 10 05 6A CD 83 FF            movups xmm0, xmmword ptr [rip - 0x7c3296]
007E6756  48 8B 0D BB 18 7F 00            mov rcx, qword ptr [rip + 0x7f18bb]
007E675D  48 8D 54 24 30                  lea rdx, [rsp + 0x30]
007E6762  F3 0F 7F 44 24 30               movdqu xmmword ptr [rsp + 0x30], xmm0
007E6768  E8 E3 BC BA FF                  call 0x140392450
007E676D  84 C0                           test al, al
007E676F  74 3B                           je 0x1407e67ac
007E6771  83 64 24 4C 00                  and dword ptr [rsp + 0x4c], 0
007E6776  48 8D 44 24 70                  lea rax, [rsp + 0x70]
007E677B  48 8B 0D 96 18 7F 00            mov rcx, qword ptr [rip + 0x7f1896]
007E6782  48 8D 54 24 30                  lea rdx, [rsp + 0x30]
007E6787  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
007E678C  41 B9 01 00 00 00               mov r9d, 1
007E6792  48 8D 44 24 40                  lea rax, [rsp + 0x40]
007E6797  C7 44 24 48 04 00 00 00         mov dword ptr [rsp + 0x48], 4
007E679F  45 33 C0                        xor r8d, r8d
007E67A2  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
007E67A7  E8 74 5F C3 FF                  call 0x14041c720
007E67AC  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
007E67B1  48 33 CC                        xor rcx, rsp
007E67B4  E8 87 5E EC FF                  call 0x1406ac640
007E67B9  48 83 C4 68                     add rsp, 0x68
007E67BD  C3                              ret
007E67BE  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpTraceHiveRestoreStop(int a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned int v_stack_m1C;
    unsigned int v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m48;
    unsigned int v_stack_p8;

    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (104);
    result = (*(unsigned __int64 *)(v_rip + 6438905)) ^ (v_rsp);
    v_stack_m18 = result;
    v_stack_m38 = v_xmm0;
    result = EtwEventEnabled(*(unsigned __int64 *)(v_rip + 8329403), v_stack_m38, a3, a4);
    if ((unsigned __int8)(result) != 0) {
        result = v_stack_p8;
        a1 = *(unsigned __int64 *)(v_rip + 8329366);
        a2 = v_stack_m38;
        v_stack_m28 = result;
        a4 = 1;
        result = v_stack_m28;
        v_stack_m20 = 4;
        a3 = 0;
        v_stack_m48 = result;
        result = EtwWrite(a1, a2, a3, a4);
    }
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (104);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t CmpTraceHiveRestoreStop(int32_t Arg1, int64_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint32_t v_stack_m1C;
    uint32_t v_stack_m20;
    uint64_t v_stack_m28;
    uint64_t v_stack_m38;
    uint64_t v_stack_m48;
    uint32_t v_stack_p8;

    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (104);
    result = (*(uint64_t *)(v_rip + 0x623FF9)) ^ (local_rsp);
    v_stack_m18 = result;
    v_stack_m38 = v_xmm0;
    result = EtwEventEnabled(*(uint64_t *)(v_rip + 0x7F18BB), v_stack_m38, Arg3, a4);
    if ((uint8_t)(result) != 0) {
        result = v_stack_p8;
        Arg1 = *(uint64_t *)(v_rip + 0x7F1896);
        Arg2 = v_stack_m38;
        v_stack_m28 = result;
        a4 = 1;
        result = v_stack_m28;
        v_stack_m20 = 4;
        Arg3 = 0;
        v_stack_m48 = result;
        result = EtwWrite(Arg1, Arg2, Arg3, a4);
    }
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, a4);
    local_rsp = (local_rsp) + (104);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007E6738&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_007E6738[BB_007E6738]
  bb_007E6771[BB_007E6771]
  bb_007E67AC[BB_007E67AC]
  bb_007E67BE[BB_007E67BE]
  bb_007E6738 -->|branch| bb_007E67AC
  bb_007E6738 -->|fallthrough| bb_007E6771
  bb_007E6771 -->|flow| bb_007E67AC
```
