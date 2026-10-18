# PspLogAuditSetLoadImageNotifyRoutineEvent

- RVA: `0x00AA1A54`–`0x00AA1AD8` (길이 `132` bytes)
- VA: `0x0000000140AA1A54`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BAD44`
- 디코드: `30`개 명령, `132/132` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00AA1AC0` → [EtwWrite](../../text/41/EtwWrite_function_0041C720.md) (function, `0x0041C720`)
- `0x00AA1ACD` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [PsSetLoadImageNotifyRoutineEx](PsSetLoadImageNotifyRoutineEx_function_00AA19A0.md) at `0x00AA1A08`

### Static image references
- `0x00AA1A63` → RVA `0x00E0A740` (`.data`; read)
- `0x00AA1A72` → RVA `0x00EFFA38` (`.data`; read)
- `0x00AA1A8C` → RVA `0x00021DC0` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x00AA1AC0` → [EtwWrite](../../text/41/EtwWrite_function_0041C720.md) (`PAGE` → `.text`)
  - `0x00AA1ACD` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00AA1A54  89 54 24 10                     mov dword ptr [rsp + 0x10], edx
00AA1A58  4C 8B DC                        mov r11, rsp
00AA1A5B  49 89 4B 08                     mov qword ptr [r11 + 8], rcx
00AA1A5F  48 83 EC 68                     sub rsp, 0x68
00AA1A63  48 8B 05 D6 8C 36 00            mov rax, qword ptr [rip + 0x368cd6]
00AA1A6A  48 33 C4                        xor rax, rsp
00AA1A6D  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
00AA1A72  48 8B 0D BF DF 45 00            mov rcx, qword ptr [rip + 0x45dfbf]
00AA1A79  48 85 C9                        test rcx, rcx
00AA1A7C  74 47                           je 0x140aa1ac5
00AA1A7E  49 8D 43 08                     lea rax, [r11 + 8]
00AA1A82  41 B9 02 00 00 00               mov r9d, 2
00AA1A88  49 89 43 C8                     mov qword ptr [r11 - 0x38], rax
00AA1A8C  48 8D 15 2D 03 58 FF            lea rdx, [rip - 0xa7fcd3]
00AA1A93  83 64 24 3C 00                  and dword ptr [rsp + 0x3c], 0
00AA1A98  49 8D 43 10                     lea rax, [r11 + 0x10]
00AA1A9C  C7 44 24 38 08 00 00 00         mov dword ptr [rsp + 0x38], 8
00AA1AA4  45 33 C0                        xor r8d, r8d
00AA1AA7  49 89 43 D8                     mov qword ptr [r11 - 0x28], rax
00AA1AAB  49 8D 43 C8                     lea rax, [r11 - 0x38]
00AA1AAF  83 64 24 4C 00                  and dword ptr [rsp + 0x4c], 0
00AA1AB4  49 89 43 B8                     mov qword ptr [r11 - 0x48], rax
00AA1AB8  C7 44 24 48 04 00 00 00         mov dword ptr [rsp + 0x48], 4
00AA1AC0  E8 5B AC 97 FF                  call 0x14041c720
00AA1AC5  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
00AA1ACA  48 33 CC                        xor rcx, rsp
00AA1ACD  E8 6E AB C0 FF                  call 0x1406ac640
00AA1AD2  48 83 C4 68                     add rsp, 0x68
00AA1AD6  C3                              ret
00AA1AD7  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PspLogAuditSetLoadImageNotifyRoutineEvent(__int64 a1, int a2, int a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned int v_stack_m1C;
    unsigned int v_stack_m20;
    unsigned int v_stack_m2C;
    unsigned int v_stack_m30;
    unsigned int v_stack_p10;

    v_stack_p10 = a2;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (104);
    result = (*(unsigned __int64 *)(v_rip + 3574998)) ^ (v_rsp);
    v_stack_m18 = result;
    if (*(unsigned __int64 *)(v_rip + 4579263) != 0) {
        result = v_rsp + 8;
        a4 = 2;
        *(unsigned __int64 *)(v_rsp - 56) = result;
        a2 = v_rip - 11009235;
        result = v_rsp + 16;
        v_stack_m30 = 8;
        a3 = 0;
        *(unsigned __int64 *)(v_rsp - 40) = result;
        result = v_rsp - 56;
        *(unsigned __int64 *)(v_rsp - 72) = result;
        v_stack_m20 = 4;
        result = EtwWrite(*(unsigned __int64 *)(v_rip + 4579263), a2, a3, a4);
    }
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (104);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PspLogAuditSetLoadImageNotifyRoutineEvent(int64_t Arg1, int32_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint32_t v_stack_m1C;
    uint32_t v_stack_m20;
    uint32_t v_stack_m2C;
    uint32_t v_stack_m30;
    uint32_t v_stack_p10;

    v_stack_p10 = Arg2;
    *(uint64_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (104);
    result = (*(uint64_t *)(v_rip + 0x368CD6)) ^ (local_rsp);
    v_stack_m18 = result;
    if (*(uint64_t *)(v_rip + 0x45DFBF) != 0) {
        result = local_rsp + 8;
        a4 = 2;
        *(uint64_t *)(local_rsp - 0x38) = result;
        Arg2 = v_rip - 11009235;
        result = local_rsp + 16;
        v_stack_m30 = 8;
        Arg3 = 0;
        *(uint64_t *)(local_rsp - 0x28) = result;
        result = local_rsp - 56;
        *(uint64_t *)(local_rsp - 0x48) = result;
        v_stack_m20 = 4;
        result = EtwWrite(*(uint64_t *)(v_rip + 0x45DFBF), Arg2, Arg3, a4);
    }
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, a4);
    local_rsp = (local_rsp) + (104);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00AA1A54&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00AA1A54[BB_00AA1A54]
  bb_00AA1A7E[BB_00AA1A7E]
  bb_00AA1AC5[BB_00AA1AC5]
  bb_00AA1AD7[BB_00AA1AD7]
  bb_00AA1A54 -->|branch| bb_00AA1AC5
  bb_00AA1A54 -->|fallthrough| bb_00AA1A7E
  bb_00AA1A7E -->|flow| bb_00AA1AC5
```
