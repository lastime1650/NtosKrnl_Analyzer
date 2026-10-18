# PopDiagTraceIdleResiliencyEnd

- RVA: `0x0046A324`–`0x0046A3D3` (길이 `175` bytes)
- VA: `0x000000014046A324`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000AB284`
- 디코드: `39`개 명령, `175/175` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x0046A354` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x0046A3C9` → [EtwWriteEx](../25/EtwWriteEx_function_0025F0D0.md) (function, `0x0025F0D0`)

### Direct callers
- [PopDeepSleepEvaluateCallback](PopDeepSleepEvaluateCallback_function_00469F10.md) at `0x00469FC3`

### Static image references
- `0x0046A335` → RVA `0x00E0A740` (`.data`; read)
- `0x0046A345` → RVA `0x00E67858` (`.data`; read)
- `0x0046A363` → RVA `0x00F0B408` (`.data`; read)
- `0x0046A3AA` → RVA `0x00019EE0` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0046A324  89 54 24 10                     mov dword ptr [rsp + 0x10], edx
0046A328  55                              push rbp
0046A329  48 8D 6C 24 A9                  lea rbp, [rsp - 0x57]
0046A32E  48 81 EC 90 00 00 00            sub rsp, 0x90
0046A335  48 8B 05 04 04 9A 00            mov rax, qword ptr [rip + 0x9a0404]
0046A33C  48 33 C4                        xor rax, rsp
0046A33F  48 89 45 47                     mov qword ptr [rbp + 0x47], rax
0046A343  33 D2                           xor edx, edx
0046A345  38 15 0D D5 9F 00               cmp byte ptr [rip + 0x9fd50d], dl
0046A34B  75 16                           jne 0x14046a363
0046A34D  48 8B 4D 47                     mov rcx, qword ptr [rbp + 0x47]
0046A351  48 33 CC                        xor rcx, rsp
0046A354  E8 E7 22 24 00                  call 0x1406ac640
0046A359  48 81 C4 90 00 00 00            add rsp, 0x90
0046A360  5D                              pop rbp
0046A361  C3                              ret
0046A362  CC                              int3
0046A363  48 8B 0D 9E 10 AA 00            mov rcx, qword ptr [rip + 0xaa109e]
0046A36A  48 8D 45 0F                     lea rax, [rbp + 0xf]
0046A36E  48 89 45 17                     mov qword ptr [rbp + 0x17], rax
0046A372  45 33 C9                        xor r9d, r9d
0046A375  48 8D 45 6F                     lea rax, [rbp + 0x6f]
0046A379  48 89 55 0F                     mov qword ptr [rbp + 0xf], rdx
0046A37D  48 89 45 27                     mov qword ptr [rbp + 0x27], rax
0046A381  45 33 C0                        xor r8d, r8d
0046A384  48 8D 45 07                     lea rax, [rbp + 7]
0046A388  89 55 07                        mov dword ptr [rbp + 7], edx
0046A38B  48 89 45 37                     mov qword ptr [rbp + 0x37], rax
0046A38F  48 8D 45 17                     lea rax, [rbp + 0x17]
0046A393  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
0046A398  C7 44 24 30 03 00 00 00         mov dword ptr [rsp + 0x30], 3
0046A3A0  48 89 54 24 28                  mov qword ptr [rsp + 0x28], rdx
0046A3A5  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
0046A3AA  48 8D 15 2F FB BA FF            lea rdx, [rip - 0x4504d1]
0046A3B1  48 C7 45 1F 04 00 00 00         mov qword ptr [rbp + 0x1f], 4
0046A3B9  48 C7 45 2F 04 00 00 00         mov qword ptr [rbp + 0x2f], 4
0046A3C1  48 C7 45 3F 04 00 00 00         mov qword ptr [rbp + 0x3f], 4
0046A3C9  E8 02 4D DF FF                  call 0x14025f0d0
0046A3CE  E9 7A FF FF FF                  jmp 0x14046a34d
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopDiagTraceIdleResiliencyEnd(__int64 a1, int a2, int a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m5F;
    unsigned int v_stack_p10;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned int v_stack_p30;
    unsigned __int64 v_stack_p38;

    v_stack_p10 = a2;
    v_rsp = (v_rsp) - (144);
    result = (*(unsigned __int64 *)(v_rip + 10093572)) ^ (v_rsp);
    v_stack_m18 = result;
    a2 = 0;
    if ((*(unsigned __int8 *)(v_rip + 10474765)) != 0) goto loc_0046A363;
loc_0046A34D:
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (144);
    return result;
loc_0046A363:
    v_stack_m48 = v_stack_m50;
    a4 = 0;
    v_stack_m50 = 0;
    v_stack_m38 = v_stack_p10;
    a3 = 0;
    v_stack_m58 = 0;
    v_stack_m28 = v_stack_m58;
    v_stack_p38 = v_stack_m48;
    v_stack_p30 = 3;
    v_stack_p28 = 0;
    v_stack_p20 = 0;
    v_stack_m40 = 4;
    v_stack_m30 = 4;
    v_stack_m20 = 4;
    result = EtwWriteEx(*(unsigned __int64 *)(v_rip + 11145374), v_rip - 4523217, a3, a4);
    goto loc_0046A34D;
}
```

## 5. (Beta) C Style

```c
int64_t PopDiagTraceIdleResiliencyEnd(int64_t Arg1, int32_t Arg2, int32_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_m20;
    uint64_t v_stack_m28;
    uint64_t v_stack_m30;
    uint64_t v_stack_m38;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m5F;
    uint32_t v_stack_p10;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint32_t v_stack_p30;
    uint64_t v_stack_p38;

    v_stack_p10 = Arg2;
    local_rsp = (local_rsp) - (144);
    result = (*(uint64_t *)(v_rip + 0x9A0404)) ^ (local_rsp);
    v_stack_m18 = result;
    Arg2 = 0;
    if ((*(uint8_t *)(v_rip + 0x9FD50D)) != 0) goto loc_0046A363;
loc_0046A34D:
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (144);
    return result;
loc_0046A363:
    v_stack_m48 = v_stack_m50;
    Arg4 = 0;
    v_stack_m50 = 0;
    v_stack_m38 = v_stack_p10;
    Arg3 = 0;
    v_stack_m58 = 0;
    v_stack_m28 = v_stack_m58;
    v_stack_p38 = v_stack_m48;
    v_stack_p30 = 3;
    v_stack_p28 = 0;
    v_stack_p20 = 0;
    v_stack_m40 = 4;
    v_stack_m30 = 4;
    v_stack_m20 = 4;
    result = EtwWriteEx(*(uint64_t *)(v_rip + 0xAA109E), v_rip - 4523217, Arg3, Arg4);
    goto loc_0046A34D;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0046A324&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0046A324[BB_0046A324]
  bb_0046A34D[BB_0046A34D]
  bb_0046A362[BB_0046A362]
  bb_0046A363[BB_0046A363]
  bb_0046A324 -->|branch| bb_0046A363
  bb_0046A324 -->|fallthrough| bb_0046A34D
  bb_0046A362 -->|flow| bb_0046A363
  bb_0046A363 -->|branch| bb_0046A34D
```
