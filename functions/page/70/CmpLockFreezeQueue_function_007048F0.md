# CmpLockFreezeQueue

- RVA: `0x007048F0`–`0x0070493C` (길이 `76` bytes)
- VA: `0x00000001407048F0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `20`개 명령, `76/76` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x00704902` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x00704927` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)

### Direct callers
- [CmThawRegistry](../7E/CmThawRegistry_function_007E8510.md) at `0x007E85FB`
- [CmpLockRegistryFreezeAware](../9B/CmpLockRegistryFreezeAware_function_009B4AE4.md) at `0x009B4B4C`

### Static image references
- `0x007048F9` → RVA `0x00EF71C0` (`.data`; read)
- `0x00704907` → RVA `0x00EF71C0` (`.data`; read/write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x00704902` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x00704927` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007048F0  40 53                           push rbx
007048F2  48 83 EC 20                     sub rsp, 0x20
007048F6  45 33 C0                        xor r8d, r8d
007048F9  48 8D 0D C0 28 7F 00            lea rcx, [rip + 0x7f28c0]
00704900  33 D2                           xor edx, edx
00704902  E8 29 B9 B0 FF                  call 0x140210230
00704907  F0 48 0F BA 2D AF 28 7F 00 00   lock bts qword ptr [rip + 0x7f28af], 0
00704911  48 8B D8                        mov rbx, rax
00704914  73 16                           jae 0x14070492c
00704916  4C 8D 05 A3 28 7F 00            lea r8, [rip + 0x7f28a3]
0070491D  48 8B D0                        mov rdx, rax
00704920  48 8D 0D 99 28 7F 00            lea rcx, [rip + 0x7f2899]
00704927  E8 64 B3 B0 FF                  call 0x14020fc90
0070492C  48 85 DB                        test rbx, rbx
0070492F  74 04                           je 0x140704935
00704931  C6 43 0A 01                     mov byte ptr [rbx + 0xa], 1
00704935  48 83 C4 20                     add rsp, 0x20
00704939  5B                              pop rbx
0070493A  C3                              ret
0070493B  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpLockFreezeQueue(__int64 a1, int a2, int a3)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(v_rip + 8333504, a2, a3, a4);
    if (!(condition_is_above_or_equal)) {
        a3 = v_rip + 8333475;
        a2 = result;
        a1 = v_rip + 8333465;
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
int64_t CmpLockFreezeQueue(int64_t Arg1, int32_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(v_rip + 8333504, Arg2, Arg3, a4);
    if (!(condition_is_above_or_equal)) {
        Arg3 = v_rip + 8333475;
        Arg2 = result;
        Arg1 = v_rip + 8333465;
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

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007048F0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_007048F0[BB_007048F0]
  bb_00704916[BB_00704916]
  bb_0070492C[BB_0070492C]
  bb_00704931[BB_00704931]
  bb_00704935[BB_00704935]
  bb_0070493B[BB_0070493B]
  bb_007048F0 -->|branch| bb_0070492C
  bb_007048F0 -->|fallthrough| bb_00704916
  bb_00704916 -->|flow| bb_0070492C
  bb_0070492C -->|branch| bb_00704935
  bb_0070492C -->|fallthrough| bb_00704931
  bb_00704931 -->|flow| bb_00704935
```
