# MiAcquireKernelCfgLock

- RVA: `0x00A4B9A0`–`0x00A4B9FD` (길이 `93` bytes)
- VA: `0x0000000140A4B9A0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `23`개 명령, `93/93` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x00A4B9C3` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x00A4B9E8` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)

### Direct callers
- [MiMarkKernelImageCfgBits](MiMarkKernelImageCfgBits_function_00A4B1E0.md) at `0x00A4B204`
- [MiAllocateKernelCfgBitmapPageTables](MiAllocateKernelCfgBitmapPageTables_function_00A4B80C.md) at `0x00A4B8A5`

### Static image references
- `0x00A4B9AF` → RVA `0x00E2D820` (`.data`; read)
- `0x00A4B9C8` → RVA `0x00E2D820` (`.data`; read/write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x00A4B9C3` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x00A4B9E8` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A4B9A0  40 53                           push rbx
00A4B9A2  48 83 EC 20                     sub rsp, 0x20
00A4B9A6  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00A4B9AF  48 8D 0D 6A 1E 3E 00            lea rcx, [rip + 0x3e1e6a]
00A4B9B6  45 33 C0                        xor r8d, r8d
00A4B9B9  33 D2                           xor edx, edx
00A4B9BB  66 FF 88 E6 01 00 00            dec word ptr [rax + 0x1e6]
00A4B9C2  90                              nop
00A4B9C3  E8 68 48 7C FF                  call 0x140210230
00A4B9C8  F0 48 0F BA 2D 4E 1E 3E 00 00   lock bts qword ptr [rip + 0x3e1e4e], 0
00A4B9D2  48 8B D8                        mov rbx, rax
00A4B9D5  73 16                           jae 0x140a4b9ed
00A4B9D7  4C 8D 05 42 1E 3E 00            lea r8, [rip + 0x3e1e42]
00A4B9DE  48 8B D0                        mov rdx, rax
00A4B9E1  48 8D 0D 38 1E 3E 00            lea rcx, [rip + 0x3e1e38]
00A4B9E8  E8 A3 42 7C FF                  call 0x14020fc90
00A4B9ED  48 85 DB                        test rbx, rbx
00A4B9F0  74 04                           je 0x140a4b9f6
00A4B9F2  C6 43 0A 01                     mov byte ptr [rbx + 0xa], 1
00A4B9F6  48 83 C4 20                     add rsp, 0x20
00A4B9FA  5B                              pop rbx
00A4B9FB  C3                              ret
00A4B9FC  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiAcquireKernelCfgLock(__int64 a1, int a2, int a3)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(v_rip + 4071018, a2, a3, a4);
    if (!(condition_is_above_or_equal)) {
        a3 = v_rip + 4070978;
        a2 = result;
        a1 = v_rip + 4070968;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiAcquireKernelCfgLock(int64_t Arg1, int32_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(v_rip + 4071018, Arg2, Arg3, a4);
    if (!(condition_is_above_or_equal)) {
        Arg3 = v_rip + 4070978;
        Arg2 = result;
        Arg1 = v_rip + 4070968;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, a4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A4B9A0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A4B9A0[BB_00A4B9A0]
  bb_00A4B9D7[BB_00A4B9D7]
  bb_00A4B9ED[BB_00A4B9ED]
  bb_00A4B9F2[BB_00A4B9F2]
  bb_00A4B9F6[BB_00A4B9F6]
  bb_00A4B9FC[BB_00A4B9FC]
  bb_00A4B9A0 -->|branch| bb_00A4B9ED
  bb_00A4B9A0 -->|fallthrough| bb_00A4B9D7
  bb_00A4B9D7 -->|flow| bb_00A4B9ED
  bb_00A4B9ED -->|branch| bb_00A4B9F6
  bb_00A4B9ED -->|fallthrough| bb_00A4B9F2
  bb_00A4B9F2 -->|flow| bb_00A4B9F6
```
