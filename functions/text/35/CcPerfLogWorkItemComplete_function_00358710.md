# CcPerfLogWorkItemComplete

- RVA: `0x00358710`–`0x00358774` (길이 `100` bytes)
- VA: `0x0000000140358710`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00079788`
- 디코드: `22`개 명령, `100/100` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0035875C` → [EtwTraceKernelEvent](../23/EtwTraceKernelEvent_function_00235350.md) (function, `0x00235350`)
- `0x00358769` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [CcAsyncLazywriteWorker](CcAsyncLazywriteWorker_function_00354C28.md) at `0x00354E99`
- [CcCachemapUninitWorkerThread](CcCachemapUninitWorkerThread_function_003569D0.md) at `0x00356B2B`
- [CcWorkerThread](../48/CcWorkerThread_function_0048F0F0.md) at `0x0048F68F`

### Static image references
- `0x00358717` → RVA `0x00E0A740` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00358710  4C 8B DC                        mov r11, rsp
00358713  48 83 EC 58                     sub rsp, 0x58
00358717  48 8B 05 22 20 AB 00            mov rax, qword ptr [rip + 0xab2022]
0035871E  48 33 C4                        xor rax, rsp
00358721  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00358726  49 8D 43 D8                     lea rax, [r11 - 0x28]
0035872A  49 89 4B D8                     mov qword ptr [r11 - 0x28], rcx
0035872E  49 89 43 E0                     mov qword ptr [r11 - 0x20], rax
00358732  49 8D 4B E0                     lea rcx, [r11 - 0x20]
00358736  83 64 24 44 00                  and dword ptr [rsp + 0x44], 0
0035873B  41 B9 02 16 00 00               mov r9d, 0x1602
00358741  BA 01 00 00 00                  mov edx, 1
00358746  C7 44 24 40 08 00 00 00         mov dword ptr [rsp + 0x40], 8
0035874E  41 B8 00 00 02 80               mov r8d, 0x80020000
00358754  C7 44 24 20 02 19 50 00         mov dword ptr [rsp + 0x20], 0x501902
0035875C  E8 EF CB ED FF                  call 0x140235350
00358761  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00358766  48 33 CC                        xor rcx, rsp
00358769  E8 D2 3E 35 00                  call 0x1406ac640
0035876E  48 83 C4 58                     add rsp, 0x58
00358772  C3                              ret
00358773  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CcPerfLogWorkItemComplete(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m10;
    unsigned int v_stack_m14;
    unsigned int v_stack_m18;
    unsigned int v_stack_m38;

    v_rsp = (v_rsp) - (88);
    result = (*(unsigned __int64 *)(v_rip + 11214882)) ^ (v_rsp);
    v_stack_m10 = result;
    *(unsigned __int64 *)(v_rsp - 40) = a1;
    *(unsigned __int64 *)(v_rsp - 32) = v_rsp - 40;
    v_stack_m18 = 8;
    v_stack_m38 = 0x501902ULL;
    result = EtwTraceKernelEvent(v_rsp - 32, 1, (unsigned int)(0x80020000ULL), (unsigned int)(0x1602ULL));
    a1 = (v_stack_m10) ^ (v_rsp);
    result = _security_check_cookie(a1, 1, (unsigned int)(0x80020000ULL), (unsigned int)(0x1602ULL));
    v_rsp = (v_rsp) + (88);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t CcPerfLogWorkItemComplete(int64_t Arg1)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m10;
    uint32_t v_stack_m14;
    uint32_t v_stack_m18;
    uint32_t v_stack_m38;

    local_rsp = (local_rsp) - (88);
    result = (*(uint64_t *)(v_rip + 0xAB2022)) ^ (local_rsp);
    v_stack_m10 = result;
    *(uint64_t *)(local_rsp - 0x28) = Arg1;
    *(uint64_t *)(local_rsp - 0x20) = local_rsp - 40;
    v_stack_m18 = 8;
    v_stack_m38 = 0x501902ULL;
    result = EtwTraceKernelEvent(local_rsp - 32, 1, (uint32_t)(0x80020000ULL), (uint32_t)(0x1602ULL));
    Arg1 = (v_stack_m10) ^ (local_rsp);
    result = _security_check_cookie(Arg1, 1, (uint32_t)(0x80020000ULL), (uint32_t)(0x1602ULL));
    local_rsp = (local_rsp) + (88);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00358710&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00358710[BB_00358710]
  bb_00358773[BB_00358773]
```
