# KiAcquireSecondarySignalListLock

- RVA: `0x005BD9B8`–`0x005BD9FC` (길이 `68` bytes)
- VA: `0x00000001405BD9B8`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CAAC`
- 디코드: `19`개 명령, `68/68` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x005BD9DD` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x005BD9EB` → [KeAcquireSpinLockAtDpcLevel](../20/KeAcquireSpinLockAtDpcLevel_function_00208430.md) (function, `0x00208430`)

### Direct callers
- [KiProcessSecondarySignalList](KiProcessSecondarySignalList_function_005BDA10.md) at `0x005BDA31`
- [sub_006F4E68](../6F/Unknown_function_006F4E68.md) at `0x006F4E6D`

### Static image references
- `0x005BD9D2` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x005BD9E2` → RVA `0x00F11038` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005BD9B8  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
005BD9BD  57                              push rdi
005BD9BE  48 83 EC 20                     sub rsp, 0x20
005BD9C2  48 8B F9                        mov rdi, rcx
005BD9C5  44 0F 20 C3                     mov rbx, cr8
005BD9C9  BA 0C 00 00 00                  mov edx, 0xc
005BD9CE  44 0F 22 C2                     mov cr8, rdx
005BD9D2  83 3D 47 93 A0 00 00            cmp dword ptr [rip + 0xa09347], 0
005BD9D9  74 07                           je 0x1405bd9e2
005BD9DB  8A CB                           mov cl, bl
005BD9DD  E8 1A 7D F3 FF                  call 0x1404f56fc
005BD9E2  48 8D 0D 4F 36 95 00            lea rcx, [rip + 0x95364f]
005BD9E9  88 1F                           mov byte ptr [rdi], bl
005BD9EB  E8 40 AA C4 FF                  call 0x140208430
005BD9F0  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
005BD9F5  48 83 C4 20                     add rsp, 0x20
005BD9F9  5F                              pop rdi
005BD9FA  C3                              ret
005BD9FB  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiAcquireSecondarySignalListLock(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    if ((*(unsigned int *)(v_rip + 10523463)) != 0) {
        a1 = (unsigned __int8)(v_cr8);
        result = KiRaiseIrqlProcessIrqlFlags(a1, 12, a3, a4);
    }
    *(unsigned __int8 *)(a1) = (unsigned __int8)(v_cr8);
    result = KeAcquireSpinLockAtDpcLevel(v_rip + 9778767, 12, a3, a4);
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t KiAcquireSecondarySignalListLock(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    if ((*(uint32_t *)(v_rip + 0xA09347)) != 0) {
        Arg1 = (uint8_t)(v_cr8);
        result = KiRaiseIrqlProcessIrqlFlags(Arg1, 12, a3, a4);
    }
    *(uint8_t *)(arg1) = (uint8_t)(v_cr8);
    result = KeAcquireSpinLockAtDpcLevel(v_rip + 9778767, 12, a3, a4);
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

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005BD9B8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005BD9B8[BB_005BD9B8]
  bb_005BD9DB[BB_005BD9DB]
  bb_005BD9E2[BB_005BD9E2]
  bb_005BD9FB[BB_005BD9FB]
  bb_005BD9B8 -->|branch| bb_005BD9E2
  bb_005BD9B8 -->|fallthrough| bb_005BD9DB
  bb_005BD9DB -->|flow| bb_005BD9E2
```
