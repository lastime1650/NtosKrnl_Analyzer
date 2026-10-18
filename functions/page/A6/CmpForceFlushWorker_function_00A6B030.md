# CmpForceFlushWorker

- RVA: `0x00A6B030`–`0x00A6B0C1` (길이 `145` bytes)
- VA: `0x0000000140A6B030`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000B42AC`
- 디코드: `37`개 명령, `145/145` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **8**; 고유 호출 대상: **8**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x00A6B06B` → [CmpInitializeThreadInfo](../../text/3F/CmpInitializeThreadInfo_function_003FBE70.md) (function, `0x003FBE70`)
- `0x00A6B070` → [CmpAcquireShutdownRundown](../../pagecmrc/BC/CmpAcquireShutdownRundown_function_00BC9400.md) (function, `0x00BC9400`)
- `0x00A6B086` → [CmCleanupThreadInfo](../../text/41/CmCleanupThreadInfo_function_0041FD50.md) (function, `0x0041FD50`)
- `0x00A6B093` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x00A6B0A4` → [CmpAttachToRegistryProcess](../../pagecmrc/BC/CmpAttachToRegistryProcess_function_00BC98E0.md) (function, `0x00BC98E0`)
- `0x00A6B0AB` → [CmpDoFlushAll](../../text/34/CmpDoFlushAll_function_00349A9C.md) (function, `0x00349A9C`)
- `0x00A6B0B5` → [CmpDetachFromRegistryProcess](../../pagecmrc/BC/CmpDetachFromRegistryProcess_function_00BC9920.md) (function, `0x00BC9920`)
- `0x00A6B0BA` → [CmpReleaseShutdownRundown](../../pagecmrc/BC/CmpReleaseShutdownRundown_function_00BC9880.md) (function, `0x00BC9880`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00A6B036` → RVA `0x00E0A740` (`.data`; read)
- `0x00A6B07B` → RVA `0x00EF7AA8` (`.data`; read/write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **8**
  - `0x00A6B06B` → [CmpInitializeThreadInfo](../../text/3F/CmpInitializeThreadInfo_function_003FBE70.md) (`PAGE` → `.text`)
  - `0x00A6B070` → [CmpAcquireShutdownRundown](../../pagecmrc/BC/CmpAcquireShutdownRundown_function_00BC9400.md) (`PAGE` → `PAGECMRC`)
  - `0x00A6B086` → [CmCleanupThreadInfo](../../text/41/CmCleanupThreadInfo_function_0041FD50.md) (`PAGE` → `.text`)
  - `0x00A6B093` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x00A6B0A4` → [CmpAttachToRegistryProcess](../../pagecmrc/BC/CmpAttachToRegistryProcess_function_00BC98E0.md) (`PAGE` → `PAGECMRC`)
  - `0x00A6B0AB` → [CmpDoFlushAll](../../text/34/CmpDoFlushAll_function_00349A9C.md) (`PAGE` → `.text`)
  - `0x00A6B0B5` → [CmpDetachFromRegistryProcess](../../pagecmrc/BC/CmpDetachFromRegistryProcess_function_00BC9920.md) (`PAGE` → `PAGECMRC`)
  - `0x00A6B0BA` → [CmpReleaseShutdownRundown](../../pagecmrc/BC/CmpReleaseShutdownRundown_function_00BC9880.md) (`PAGE` → `PAGECMRC`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A6B030  40 53                           push rbx
00A6B032  48 83 EC 70                     sub rsp, 0x70
00A6B036  48 8B 05 03 F7 39 00            mov rax, qword ptr [rip + 0x39f703]
00A6B03D  48 33 C4                        xor rax, rsp
00A6B040  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
00A6B045  0F 57 C9                        xorps xmm1, xmm1
00A6B048  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00A6B04D  0F 57 C0                        xorps xmm0, xmm0
00A6B050  33 C0                           xor eax, eax
00A6B052  0F 11 44 24 20                  movups xmmword ptr [rsp + 0x20], xmm0
00A6B057  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00A6B05C  0F 11 4C 24 38                  movups xmmword ptr [rsp + 0x38], xmm1
00A6B061  0F 11 4C 24 48                  movups xmmword ptr [rsp + 0x48], xmm1
00A6B066  0F 11 4C 24 58                  movups xmmword ptr [rsp + 0x58], xmm1
00A6B06B  E8 00 0E 99 FF                  call 0x1403fbe70
00A6B070  E8 8B E3 15 00                  call 0x140bc9400
00A6B075  33 DB                           xor ebx, ebx
00A6B077  84 C0                           test al, al
00A6B079  75 24                           jne 0x140a6b09f
00A6B07B  87 1D 27 CA 48 00               xchg dword ptr [rip + 0x48ca27], ebx
00A6B081  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00A6B086  E8 C5 4C 9B FF                  call 0x14041fd50
00A6B08B  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
00A6B090  48 33 CC                        xor rcx, rsp
00A6B093  E8 A8 15 C4 FF                  call 0x1406ac640
00A6B098  48 83 C4 70                     add rsp, 0x70
00A6B09C  5B                              pop rbx
00A6B09D  C3                              ret
00A6B09E  CC                              int3
00A6B09F  48 8D 4C 24 38                  lea rcx, [rsp + 0x38]
00A6B0A4  E8 37 E8 15 00                  call 0x140bc98e0
00A6B0A9  33 C9                           xor ecx, ecx
00A6B0AB  E8 EC E9 8D FF                  call 0x140349a9c
00A6B0B0  48 8D 4C 24 38                  lea rcx, [rsp + 0x38]
00A6B0B5  E8 66 E8 15 00                  call 0x140bc9920
00A6B0BA  E8 C1 E7 15 00                  call 0x140bc9880
00A6B0BF  EB BA                           jmp 0x140a6b07b
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpForceFlushWorker(void)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m10;
    unsigned __int64 v_stack_m20;
    unsigned __int64 v_stack_m30;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_p38;

    v_rsp = (v_rsp) - (112);
    result = (*(unsigned __int64 *)(v_rip + 3798787)) ^ (v_rsp);
    v_stack_m10 = result;
    result = 0;
    v_stack_m58 = v_xmm0;
    v_stack_m48 = 0;
    v_stack_m40 = v_xmm1;
    v_stack_m30 = v_xmm1;
    v_stack_m20 = v_xmm1;
    result = CmpInitializeThreadInfo(v_stack_m58, a2, a3, a4);
    result = CmpAcquireShutdownRundown(v_stack_m58, a2, a3, a4);
    v_rbx = 0;
    if ((unsigned __int8)(result) != 0) goto loc_00A6B09F;
loc_00A6B07B:
    result = CmCleanupThreadInfo(v_stack_m58, a2, a3, a4);
    a1 = (v_stack_m10) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (112);
    return result;
loc_00A6B09F:
    result = CmpAttachToRegistryProcess(v_stack_p38, a2, a3, a4);
    a1 = 0;
    result = CmpDoFlushAll(a1, a2, a3, a4);
    result = CmpDetachFromRegistryProcess(v_stack_p38, a2, a3, a4);
    result = CmpReleaseShutdownRundown(v_stack_p38, a2, a3, a4);
    goto loc_00A6B07B;
}
```

## 5. (Beta) C Style

```c
void CmpForceFlushWorker(void)
{
    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m10;
    uint64_t v_stack_m20;
    uint64_t v_stack_m30;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m58;
    uint64_t v_stack_p38;

    local_rsp = (local_rsp) - (112);
    result = (*(uint64_t *)(v_rip + 0x39F703)) ^ (local_rsp);
    v_stack_m10 = result;
    result = 0;
    v_stack_m58 = v_xmm0;
    v_stack_m48 = 0;
    v_stack_m40 = v_xmm1;
    v_stack_m30 = v_xmm1;
    v_stack_m20 = v_xmm1;
    result = CmpInitializeThreadInfo(v_stack_m58, a2, a3, a4);
    result = CmpAcquireShutdownRundown(v_stack_m58, a2, a3, a4);
    local_rbx = 0;
    if ((uint8_t)(result) != 0) goto loc_00A6B09F;
loc_00A6B07B:
    result = CmCleanupThreadInfo(v_stack_m58, a2, a3, a4);
    a1 = (v_stack_m10) ^ (local_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    local_rsp = (local_rsp) + (112);
    return result;
loc_00A6B09F:
    result = CmpAttachToRegistryProcess(v_stack_p38, a2, a3, a4);
    a1 = 0;
    result = CmpDoFlushAll(a1, a2, a3, a4);
    result = CmpDetachFromRegistryProcess(v_stack_p38, a2, a3, a4);
    result = CmpReleaseShutdownRundown(v_stack_p38, a2, a3, a4);
    goto loc_00A6B07B;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A6B030&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A6B030[BB_00A6B030]
  bb_00A6B07B[BB_00A6B07B]
  bb_00A6B09E[BB_00A6B09E]
  bb_00A6B09F[BB_00A6B09F]
  bb_00A6B030 -->|branch| bb_00A6B09F
  bb_00A6B030 -->|fallthrough| bb_00A6B07B
  bb_00A6B09E -->|flow| bb_00A6B09F
  bb_00A6B09F -->|branch| bb_00A6B07B
```
