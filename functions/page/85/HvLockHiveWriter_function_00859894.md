# HvLockHiveWriter

- RVA: `0x00859894`–`0x008598DD` (길이 `73` bytes)
- VA: `0x0000000140859894`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CAAC`
- 디코드: `23`개 명령, `73/73` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **23**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x008598AA` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x008598C3` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)

### Direct callers
- [CmpLoadHiveThread](../7D/CmpLoadHiveThread_function_007DB040.md) at `0x007DB7CB`
- [CmpMountPreloadedHives](../7D/CmpMountPreloadedHives_function_007DBE18.md) at `0x007DC257`
- [CmpMountPreloadedHives](../7D/CmpMountPreloadedHives_function_007DBE18.md) at `0x007DC2B2`
- [CmpRefreshHive](../7D/CmpRefreshHive_function_007DEAD0.md) at `0x007DEBC8`
- [CmFreezeRegistry](../7E/CmFreezeRegistry_function_007E834C.md) at `0x007E841F`
- [CmThawRegistry](../7E/CmThawRegistry_function_007E8510.md) at `0x007E85C2`
- [CmpRecoverFlushProtocolStateFromFiles](../7E/CmpRecoverFlushProtocolStateFromFiles_function_007EE4B0.md) at `0x007EE4FB`
- [HvIsRangeDirty](../7F/HvIsRangeDirty_function_007F39BC.md) at `0x007F39E1`
- [HvMarkCellDirty](HvMarkCellDirty_function_00859758.md) at `0x00859799`
- [HvAllocateCell](HvAllocateCell_function_00859C94.md) at `0x00859D10`
- [sub_00859FB9](Unknown_function_00859FB9.md) at `0x0085A011`
- [HvFreeCell](HvFreeCell_function_0085A72C.md) at `0x0085A764`
- [CmpCreateHive](../87/CmpCreateHive_function_00879DF0.md) at `0x0087A20B`
- [CmpReorganizeHive](../87/CmpReorganizeHive_function_0087B92C.md) at `0x0087BADD`
- [CmpInitCmRM](../87/CmpInitCmRM_function_0087C700.md) at `0x0087CE67`
- [CmpTransMgrSyncHive](../9B/CmpTransMgrSyncHive_function_009B07C4.md) at `0x009B0821`
- [CmpTransMgrPrepare](../9B/CmpTransMgrPrepare_function_009B175C.md) at `0x009B1904`
- [CmpFlushHive](../9B/CmpFlushHive_function_009B3DC0.md) at `0x009B447C`
- [CmpDoLocalizeNextHive](../9B/CmpDoLocalizeNextHive_function_009B7400.md) at `0x009B743D`
- [HvFoldBackDirtyData](../A4/HvFoldBackDirtyData_function_00A463B8.md) at `0x00A463FE`
- [CmpTrimHive](../A4/CmpTrimHive_function_00A4F2FC.md) at `0x00A4F33E`
- [CmpMarkEntireIndexDirty](../AA/CmpMarkEntireIndexDirty_function_00AA24B4.md) at `0x00AA24F8`
- [CmpCreateHiveRootCell](../AB/CmpCreateHiveRootCell_function_00ABF568.md) at `0x00ABF746`
- [sub_00B1845C](../B1/Unknown_function_00B1845C.md) at `0x00B186D3`
- [sub_00B1845C](../B1/Unknown_function_00B1845C.md) at `0x00B187CB`
- [sub_00B1845C](../B1/Unknown_function_00B1845C.md) at `0x00B188E8`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x008598AA` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x008598C3` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00859894  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00859899  57                              push rdi
0085989A  48 83 EC 20                     sub rsp, 0x20
0085989E  48 8D 79 50                     lea rdi, [rcx + 0x50]
008598A2  45 33 C0                        xor r8d, r8d
008598A5  48 8B CF                        mov rcx, rdi
008598A8  33 D2                           xor edx, edx
008598AA  E8 81 69 9B FF                  call 0x140210230
008598AF  F0 48 0F BA 2F 00               lock bts qword ptr [rdi], 0
008598B5  48 8B D8                        mov rbx, rax
008598B8  73 0E                           jae 0x1408598c8
008598BA  4C 8B C7                        mov r8, rdi
008598BD  48 8B D0                        mov rdx, rax
008598C0  48 8B CF                        mov rcx, rdi
008598C3  E8 C8 63 9B FF                  call 0x14020fc90
008598C8  48 85 DB                        test rbx, rbx
008598CB  74 04                           je 0x1408598d1
008598CD  C6 43 0A 01                     mov byte ptr [rbx + 0xa], 1
008598D1  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
008598D6  48 83 C4 20                     add rsp, 0x20
008598DA  5F                              pop rdi
008598DB  C3                              ret
008598DC  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HvLockHiveWriter(__int64 a1, int a2, int a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(a1 + 80, a2, a3, a4);
    if (!(condition_is_above_or_equal)) {
        a3 = a1 + 80;
        a2 = result;
        a1 = a1 + 80;
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
int64_t HvLockHiveWriter(void *Arg1, int32_t Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(Arg1 + 80, Arg2, Arg3, a4);
    if (!(condition_is_above_or_equal)) {
        Arg3 = Arg1 + 80;
        Arg2 = result;
        Arg1 = Arg1 + 80;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, a4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R/W` |
| `Arg1` | `+ 0x50` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00859894&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00859894[BB_00859894]
  bb_008598BA[BB_008598BA]
  bb_008598C8[BB_008598C8]
  bb_008598CD[BB_008598CD]
  bb_008598D1[BB_008598D1]
  bb_008598DC[BB_008598DC]
  bb_00859894 -->|branch| bb_008598C8
  bb_00859894 -->|fallthrough| bb_008598BA
  bb_008598BA -->|flow| bb_008598C8
  bb_008598C8 -->|branch| bb_008598D1
  bb_008598C8 -->|fallthrough| bb_008598CD
  bb_008598CD -->|flow| bb_008598D1
```
