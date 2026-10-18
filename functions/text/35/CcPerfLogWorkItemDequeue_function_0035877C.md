# CcPerfLogWorkItemDequeue

- RVA: `0x0035877C`–`0x003587E0` (길이 `100` bytes)
- VA: `0x000000014035877C`
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
- `0x003587C8` → [EtwTraceKernelEvent](../23/EtwTraceKernelEvent_function_00235350.md) (function, `0x00235350`)
- `0x003587D5` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [CcAsyncLazywriteWorker](CcAsyncLazywriteWorker_function_00354C28.md) at `0x00354D63`
- [CcCachemapUninitWorkerThread](CcCachemapUninitWorkerThread_function_003569D0.md) at `0x00356AC8`
- [CcWorkerThread](../48/CcWorkerThread_function_0048F0F0.md) at `0x0048F669`

### Static image references
- `0x00358783` → RVA `0x00E0A740` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0035877C  4C 8B DC                        mov r11, rsp
0035877F  48 83 EC 58                     sub rsp, 0x58
00358783  48 8B 05 B6 1F AB 00            mov rax, qword ptr [rip + 0xab1fb6]
0035878A  48 33 C4                        xor rax, rsp
0035878D  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00358792  49 8D 43 D8                     lea rax, [r11 - 0x28]
00358796  49 89 4B D8                     mov qword ptr [r11 - 0x28], rcx
0035879A  49 89 43 E0                     mov qword ptr [r11 - 0x20], rax
0035879E  49 8D 4B E0                     lea rcx, [r11 - 0x20]
003587A2  83 64 24 44 00                  and dword ptr [rsp + 0x44], 0
003587A7  41 B9 01 16 00 00               mov r9d, 0x1601
003587AD  BA 01 00 00 00                  mov edx, 1
003587B2  C7 44 24 40 08 00 00 00         mov dword ptr [rsp + 0x40], 8
003587BA  41 B8 00 00 02 80               mov r8d, 0x80020000
003587C0  C7 44 24 20 02 19 50 00         mov dword ptr [rsp + 0x20], 0x501902
003587C8  E8 83 CB ED FF                  call 0x140235350
003587CD  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
003587D2  48 33 CC                        xor rcx, rsp
003587D5  E8 66 3E 35 00                  call 0x1406ac640
003587DA  48 83 C4 58                     add rsp, 0x58
003587DE  C3                              ret
003587DF  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CcPerfLogWorkItemDequeue(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m10;
    unsigned int v_stack_m14;
    unsigned int v_stack_m18;
    unsigned int v_stack_m38;

    v_rsp = (v_rsp) - (88);
    result = (*(unsigned __int64 *)(v_rip + 11214774)) ^ (v_rsp);
    v_stack_m10 = result;
    *(unsigned __int64 *)(v_rsp - 40) = a1;
    *(unsigned __int64 *)(v_rsp - 32) = v_rsp - 40;
    v_stack_m18 = 8;
    v_stack_m38 = 0x501902ULL;
    result = EtwTraceKernelEvent(v_rsp - 32, 1, (unsigned int)(0x80020000ULL), (unsigned int)(0x1601ULL));
    a1 = (v_stack_m10) ^ (v_rsp);
    result = _security_check_cookie(a1, 1, (unsigned int)(0x80020000ULL), (unsigned int)(0x1601ULL));
    v_rsp = (v_rsp) + (88);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t CcPerfLogWorkItemDequeue(int64_t Arg1)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m10;
    uint32_t v_stack_m14;
    uint32_t v_stack_m18;
    uint32_t v_stack_m38;

    local_rsp = (local_rsp) - (88);
    result = (*(uint64_t *)(v_rip + 0xAB1FB6)) ^ (local_rsp);
    v_stack_m10 = result;
    *(uint64_t *)(local_rsp - 0x28) = Arg1;
    *(uint64_t *)(local_rsp - 0x20) = local_rsp - 40;
    v_stack_m18 = 8;
    v_stack_m38 = 0x501902ULL;
    result = EtwTraceKernelEvent(local_rsp - 32, 1, (uint32_t)(0x80020000ULL), (uint32_t)(0x1601ULL));
    Arg1 = (v_stack_m10) ^ (local_rsp);
    result = _security_check_cookie(Arg1, 1, (uint32_t)(0x80020000ULL), (uint32_t)(0x1601ULL));
    local_rsp = (local_rsp) + (88);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0035877C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0035877C[BB_0035877C]
  bb_003587DF[BB_003587DF]
```
