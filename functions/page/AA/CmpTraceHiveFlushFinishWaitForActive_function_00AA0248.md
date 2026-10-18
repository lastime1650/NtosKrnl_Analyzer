# CmpTraceHiveFlushFinishWaitForActive

- RVA: `0x00AA0248`–`0x00AA02AF` (길이 `103` bytes)
- VA: `0x0000000140AA0248`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0009E910`
- 디코드: `24`개 명령, `103/103` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00AA0274` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (function, `0x00392450`)
- `0x00AA0285` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x00AA02A8` → [EtwWrite](../../text/41/EtwWrite_function_0041C720.md) (function, `0x0041C720`)

### Direct callers
- [CmpWaitOnHiveWriteQueue](CmpWaitOnHiveWriteQueue_function_00AA0110.md) at `0x00AA019A`

### Static image references
- `0x00AA024C` → RVA `0x00E0A740` (`.data`; read)
- `0x00AA025B` → RVA `0x0001C770` (`.rdata`; read)
- `0x00AA0262` → RVA `0x00FD8018` (`PAGEDATA`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x00AA0274` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (`PAGE` → `.text`)
  - `0x00AA0285` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x00AA02A8` → [EtwWrite](../../text/41/EtwWrite_function_0041C720.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00AA0248  48 83 EC 58                     sub rsp, 0x58
00AA024C  48 8B 05 ED A4 36 00            mov rax, qword ptr [rip + 0x36a4ed]
00AA0253  48 33 C4                        xor rax, rsp
00AA0256  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00AA025B  0F 10 05 0E C5 57 FF            movups xmm0, xmmword ptr [rip - 0xa83af2]
00AA0262  48 8B 0D AF 7D 53 00            mov rcx, qword ptr [rip + 0x537daf]
00AA0269  48 8D 54 24 30                  lea rdx, [rsp + 0x30]
00AA026E  F3 0F 7F 44 24 30               movdqu xmmword ptr [rsp + 0x30], xmm0
00AA0274  E8 D7 21 8F FF                  call 0x140392450
00AA0279  84 C0                           test al, al
00AA027B  75 13                           jne 0x140aa0290
00AA027D  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AA0282  48 33 CC                        xor rcx, rsp
00AA0285  E8 B6 C3 C0 FF                  call 0x1406ac640
00AA028A  48 83 C4 58                     add rsp, 0x58
00AA028E  C3                              ret
00AA028F  CC                              int3
00AA0290  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
00AA0296  48 8D 54 24 30                  lea rdx, [rsp + 0x30]
00AA029B  48 8B 0D 76 7D 53 00            mov rcx, qword ptr [rip + 0x537d76]
00AA02A2  45 33 C9                        xor r9d, r9d
00AA02A5  45 33 C0                        xor r8d, r8d
00AA02A8  E8 73 C4 97 FF                  call 0x14041c720
00AA02AD  EB CE                           jmp 0x140aa027d
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpTraceHiveFlushFinishWaitForActive(__int64 a1, __int64 a2, int a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p30;

    v_rsp = (v_rsp) - (88);
    result = (*(unsigned __int64 *)(v_rip + 3581165)) ^ (v_rsp);
    v_stack_m18 = result;
    v_stack_m28 = v_xmm0;
    result = EtwEventEnabled(*(unsigned __int64 *)(v_rip + 5471663), v_stack_m28, a3, a4);
    if ((unsigned __int8)(result) != 0) goto loc_00AA0290;
loc_00AA027D:
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, v_stack_m28, a3, a4);
    v_rsp = (v_rsp) + (88);
    return result;
loc_00AA0290:
    a4 = 0;
    a3 = 0;
    result = EtwWrite(*(unsigned __int64 *)(v_rip + 5471606), v_stack_p30, a3, a4);
    goto loc_00AA027D;
}
```

## 5. (Beta) C Style

```c
int64_t CmpTraceHiveFlushFinishWaitForActive(int64_t Arg1, int64_t Arg2, int32_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_m28;
    uint64_t v_stack_p20;
    uint64_t v_stack_p30;

    local_rsp = (local_rsp) - (88);
    result = (*(uint64_t *)(v_rip + 0x36A4ED)) ^ (local_rsp);
    v_stack_m18 = result;
    v_stack_m28 = v_xmm0;
    result = EtwEventEnabled(*(uint64_t *)(v_rip + 0x537DAF), v_stack_m28, Arg3, Arg4);
    if ((uint8_t)(result) != 0) goto loc_00AA0290;
loc_00AA027D:
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, v_stack_m28, Arg3, Arg4);
    local_rsp = (local_rsp) + (88);
    return result;
loc_00AA0290:
    Arg4 = 0;
    Arg3 = 0;
    result = EtwWrite(*(uint64_t *)(v_rip + 0x537D76), v_stack_p30, Arg3, Arg4);
    goto loc_00AA027D;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00AA0248&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00AA0248[BB_00AA0248]
  bb_00AA027D[BB_00AA027D]
  bb_00AA028F[BB_00AA028F]
  bb_00AA0290[BB_00AA0290]
  bb_00AA0248 -->|branch| bb_00AA0290
  bb_00AA0248 -->|fallthrough| bb_00AA027D
  bb_00AA028F -->|flow| bb_00AA0290
  bb_00AA0290 -->|branch| bb_00AA027D
```
