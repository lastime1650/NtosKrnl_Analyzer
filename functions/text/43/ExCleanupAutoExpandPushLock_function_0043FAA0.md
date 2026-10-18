# ExCleanupAutoExpandPushLock

- RVA: `0x0043FAA0`–`0x0043FAC3` (길이 `35` bytes)
- VA: `0x000000014043FAA0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `11`개 명령, `35/35` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0043FAB8` → [ExSaFree](ExSaFree_function_0043FACC.md) (function, `0x0043FACC`)

### Direct callers
- [MiDeleteAweInfo](../../page/80/MiDeleteAweInfo_function_0080A9F8.md) at `0x0080AA13`
- [sub_00863F57](../../page/86/Unknown_function_00863F57.md) at `0x00863FF2`
- [FsRtlTeardownPerFileContexts](../../page/A0/FsRtlTeardownPerFileContexts_function_00A0CDD0.md) at `0x00A0CE84`
- [MmDeleteProcessAddressSpace](../../page/AC/MmDeleteProcessAddressSpace_function_00AC804C.md) at `0x00AC8198`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0043FAA0  48 83 EC 28                     sub rsp, 0x28
0043FAA4  8B 41 08                        mov eax, dword ptr [rcx + 8]
0043FAA7  A8 01                           test al, 1
0043FAA9  74 12                           je 0x14043fabd
0043FAAB  B9 F8 FF FF FF                  mov ecx, 0xfffffff8
0043FAB0  BA 10 00 00 00                  mov edx, 0x10
0043FAB5  48 23 C8                        and rcx, rax
0043FAB8  E8 0F 00 00 00                  call 0x14043facc
0043FABD  48 83 C4 28                     add rsp, 0x28
0043FAC1  C3                              ret
0043FAC2  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ExCleanupAutoExpandPushLock(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = (unsigned int)(*(unsigned int *)(a1 + 8));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 8)))) & (1)) != 0) {
        a1 = 0xFFFFFFF8ULL;
        a2 = 16;
        a1 = (a1) & ((unsigned int)(*(unsigned int *)(a1 + 8)));
        result = ExSaFree(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t ExCleanupAutoExpandPushLock(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = (uint32_t)(*(uint32_t *)(arg1 + 0x8));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x8)))) & (1)) != 0) {
        Arg1 = 0xFFFFFFF8ULL;
        a2 = 16;
        Arg1 = (Arg1) & ((uint32_t)(*(uint32_t *)(arg1 + 0x8)));
        result = ExSaFree(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x8` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0043FAA0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0043FAA0[BB_0043FAA0]
  bb_0043FAAB[BB_0043FAAB]
  bb_0043FABD[BB_0043FABD]
  bb_0043FAC2[BB_0043FAC2]
  bb_0043FAA0 -->|branch| bb_0043FABD
  bb_0043FAA0 -->|fallthrough| bb_0043FAAB
  bb_0043FAAB -->|flow| bb_0043FABD
```
