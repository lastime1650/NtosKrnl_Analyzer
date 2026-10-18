# PopSessionDisconnected

- RVA: `0x00912BD8`–`0x00912C56` (길이 `126` bytes)
- VA: `0x0000000140912BD8`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CAAC`
- 디코드: `35`개 명령, `126/126` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **4**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **5**

### Outgoing calls
- `0x00912BF3` → [PopDiagTraceSessionState](PopDiagTraceSessionState_function_00912C5C.md) (function, `0x00912C5C`)
- `0x00912C12` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00912C2F` → [PopSetSessionDisplayStatus](PopSetSessionDisplayStatus_function_00912E7C.md) (function, `0x00912E7C`)
- `0x00912C3B` → [PopSetSessionUserStatus](PopSetSessionUserStatus_function_00914BB8.md) (function, `0x00914BB8`)

### Direct callers
- [PopSessionConnectionChange](../76/PopSessionConnectionChange_function_0076BDEC.md) at `0x0076BE79`
- [PopSessionConnectionChangeV2](../76/PopSessionConnectionChangeV2_function_0076BEA8.md) at `0x0076BF34`

### Static image references
- `0x00912BEC` → RVA `0x00011A08` (`.rdata`; read)
- `0x00912BF8` → RVA `0x00F08238` (`.data`; read)
- `0x00912C07` → RVA `0x00F08220` (`.data`; read)
- `0x00912C17` → RVA `0x00F08238` (`.data`; read/write)
- `0x00912C1E` → RVA `0x00F0823C` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00912C12` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00912BD8  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00912BDD  57                              push rdi
00912BDE  48 83 EC 20                     sub rsp, 0x20
00912BE2  48 8B FA                        mov rdi, rdx
00912BE5  8B D9                           mov ebx, ecx
00912BE7  8B D1                           mov edx, ecx
00912BE9  45 33 C0                        xor r8d, r8d
00912BEC  48 8D 0D 15 EE 6F FF            lea rcx, [rip - 0x9011eb]
00912BF3  E8 64 00 00 00                  call 0x140912c5c
00912BF8  39 1D 3A 56 5F 00               cmp dword ptr [rip + 0x5f563a], ebx
00912BFE  75 28                           jne 0x140912c28
00912C00  83 FB FF                        cmp ebx, -1
00912C03  74 23                           je 0x140912c28
00912C05  33 D2                           xor edx, edx
00912C07  48 8D 0D 12 56 5F 00            lea rcx, [rip + 0x5f5612]
00912C0E  44 8D 42 50                     lea r8d, [rdx + 0x50]
00912C12  E8 29 40 DB FF                  call 0x1406c6c40
00912C17  83 0D 1A 56 5F 00 FF            or dword ptr [rip + 0x5f561a], 0xffffffff
00912C1E  C7 05 14 56 5F 00 03 00 00 00   mov dword ptr [rip + 0x5f5614], 3
00912C28  45 33 C0                        xor r8d, r8d
00912C2B  33 D2                           xor edx, edx
00912C2D  8B CB                           mov ecx, ebx
00912C2F  E8 48 02 00 00                  call 0x140912e7c
00912C34  BA 02 00 00 00                  mov edx, 2
00912C39  8B CB                           mov ecx, ebx
00912C3B  E8 78 1F 00 00                  call 0x140914bb8
00912C40  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
00912C45  33 C0                           xor eax, eax
00912C47  89 07                           mov dword ptr [rdi], eax
00912C49  89 47 08                        mov dword ptr [rdi + 8], eax
00912C4C  88 47 0C                        mov byte ptr [rdi + 0xc], al
00912C4F  48 83 C4 20                     add rsp, 0x20
00912C53  5F                              pop rdi
00912C54  C3                              ret
00912C55  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopSessionDisconnected(int a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    a3 = 0;
    result = PopDiagTraceSessionState(v_rip - 9441771, (unsigned int)(a1), a3, a4);
    if ((*(unsigned int *)(v_rip + 6247994)) != ((unsigned int)((unsigned int)(a1)))) goto loc_00912C28;
    if (((unsigned int)((unsigned int)(a1))) != -1) {
        a2 = 0;
        a1 = v_rip + 6247954;
        a3 = a2 + 80;
        result = memset(a1, a2, a3, a4);
        *(unsigned int *)(v_rip + 6247956) = 3;
    }
    a3 = 0;
    a2 = 0;
    result = PopSetSessionDisplayStatus((unsigned int)((unsigned int)((unsigned int)(a1))), a2, a3, a4);
    result = PopSetSessionUserStatus((unsigned int)((unsigned int)((unsigned int)(a1))), 2, a3, a4);
    result = 0;
    *(unsigned int *)(a2) = 0;
    *(unsigned int *)(a2 + 8) = 0;
    *(unsigned __int8 *)(a2 + 12) = 0;
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PopSessionDisconnected(int32_t Arg1, void *Arg2, int32_t Arg3)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    Arg3 = 0;
    result = PopDiagTraceSessionState(v_rip - 9441771, (uint32_t)(Arg1), Arg3, a4);
    if ((*(uint32_t *)(v_rip + 0x5F563A)) != ((uint32_t)((uint32_t)(Arg1)))) goto loc_00912C28;
    if (((uint32_t)((uint32_t)(Arg1))) != -1) {
        Arg2 = 0;
        Arg1 = v_rip + 6247954;
        Arg3 = Arg2 + 80;
        result = memset(Arg1, Arg2, Arg3, a4);
        *(uint32_t *)(v_rip + 0x5F5614) = 3;
    }
    Arg3 = 0;
    Arg2 = 0;
    result = PopSetSessionDisplayStatus((uint32_t)((uint32_t)((uint32_t)(Arg1))), Arg2, Arg3, a4);
    result = PopSetSessionUserStatus((uint32_t)((uint32_t)((uint32_t)(Arg1))), 2, Arg3, a4);
    result = 0;
    *(uint32_t *)(arg2) = 0;
    *(uint32_t *)(arg2 + 0x8) = 0;
    *(uint8_t *)(arg2 + 0xC) = 0;
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0` | `32` | `W` |
| `Arg2` | `+ 0x8` | `32` | `W` |
| `Arg2` | `+ 0xC` | `8` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00912BD8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00912BD8[BB_00912BD8]
  bb_00912C00[BB_00912C00]
  bb_00912C05[BB_00912C05]
  bb_00912C28[BB_00912C28]
  bb_00912C55[BB_00912C55]
  bb_00912BD8 -->|branch| bb_00912C28
  bb_00912BD8 -->|fallthrough| bb_00912C00
  bb_00912C00 -->|branch| bb_00912C28
  bb_00912C00 -->|fallthrough| bb_00912C05
  bb_00912C05 -->|flow| bb_00912C28
```
