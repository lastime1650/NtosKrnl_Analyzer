# ViIrpDatabaseAcquireLockExclusive

- RVA: `0x006176D8`–`0x006176F6` (길이 `30` bytes)
- VA: `0x00000001406176D8`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `10`개 명령, `30/30` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **6**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x006176E8` → [ExAcquireSpinLockExclusive](../24/ExAcquireSpinLockExclusive_function_00248690.md) (function, `0x00248690`)

### Direct callers
- [ViPendingCompleteAfterWait](../../pagevrfy/BA/ViPendingCompleteAfterWait_function_00BA1D18.md) at `0x00BA1D96`
- [VfIrpDatabaseEntryInsertAndLock](../../pagevrfy/BB/VfIrpDatabaseEntryInsertAndLock_function_00BB3F00.md) at `0x00BB3F4C`
- [VfIrpDatabaseEntryReleaseLock](../../pagevrfy/BB/VfIrpDatabaseEntryReleaseLock_function_00BB3FD4.md) at `0x00BB3FF6`
- [VfIrpDatabaseEntryReleaseLock](../../pagevrfy/BB/VfIrpDatabaseEntryReleaseLock_function_00BB3FD4.md) at `0x00BB404E`
- [sub_00BBBE00](../../pagevrfy/BB/Unknown_function_00BBBE00.md) at `0x00BBC008`
- [sub_00BBC0C8](../../pagevrfy/BB/Unknown_function_00BBC0C8.md) at `0x00BBC114`
- [sub_00BBC0C8](../../pagevrfy/BB/Unknown_function_00BBC0C8.md) at `0x00BBC1A2`
- [sub_00BBC208](../../pagevrfy/BB/Unknown_function_00BBC208.md) at `0x00BBC259`

### Static image references
- `0x006176E1` → RVA `0x00F04888` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006176D8  40 53                           push rbx
006176DA  48 83 EC 20                     sub rsp, 0x20
006176DE  48 8B D9                        mov rbx, rcx
006176E1  48 8D 0D A0 D1 8E 00            lea rcx, [rip + 0x8ed1a0]
006176E8  E8 A3 0F C3 FF                  call 0x140248690
006176ED  88 03                           mov byte ptr [rbx], al
006176EF  48 83 C4 20                     add rsp, 0x20
006176F3  5B                              pop rbx
006176F4  C3                              ret
006176F5  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ViIrpDatabaseAcquireLockExclusive(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    result = ExAcquireSpinLockExclusive(v_rip + 9359776, a2, a3, a4);
    *(unsigned __int8 *)(a1) = (unsigned __int8)(result);
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t ViIrpDatabaseAcquireLockExclusive(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    result = ExAcquireSpinLockExclusive(v_rip + 9359776, a2, a3, a4);
    *(uint8_t *)(arg1) = (uint8_t)(result);
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `8` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006176D8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006176D8[BB_006176D8]
  bb_006176F5[BB_006176F5]
```
