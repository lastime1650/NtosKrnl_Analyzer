# CmpAllocateTransientPoolWithQuota

- RVA: `0x00461190`–`0x004611A4` (길이 `20` bytes)
- VA: `0x0000000140461190`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `6`개 명령, `20/20` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **13**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00461199` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)

### Direct callers
- [NtCompactKeys](../../page/7D/NtCompactKeys_function_007DF730.md) at `0x007DF7E0`
- [NtQueryOpenSubKeysEx](../../page/7E/NtQueryOpenSubKeysEx_function_007E0190.md) at `0x007E031A`
- [NtRenameKey](../../page/7E/NtRenameKey_function_007E04B0.md) at `0x007E0672`
- [NtSetValueKey](../../page/84/NtSetValueKey_function_00844EA0.md) at `0x008451F9`
- [NtDeleteValueKey](../../page/84/NtDeleteValueKey_function_00848770.md) at `0x0084897E`
- [NtQueryKey](../../page/86/NtQueryKey_function_008676E0.md) at `0x00867EA2`
- [CmCreateKey](../../page/87/CmCreateKey_function_00875020.md) at `0x00875203`
- [CmLoadDifferencingKey](../../page/87/CmLoadDifferencingKey_function_00875670.md) at `0x00875933`
- [CmpCaptureKeyValueArray](../../page/8B/CmpCaptureKeyValueArray_function_008B1074.md) at `0x008B10CB`
- [CmpCaptureKeyValueArray](../../page/8B/CmpCaptureKeyValueArray_function_008B1074.md) at `0x008B10F3`
- [CmpCaptureKeyValueArray](../../page/8B/CmpCaptureKeyValueArray_function_008B1074.md) at `0x008B1267`
- [sub_008B2988](../../page/8B/Unknown_function_008B2988.md) at `0x008B2991`
- [NtQueryValueKey](../../page/8B/NtQueryValueKey_function_008B2A00.md) at `0x008B2C6C`
- [NtEnumerateValueKey](../../page/8B/NtEnumerateValueKey_function_008B3B50.md) at `0x008B43D3`
- [CmUnloadKey](../../page/9A/CmUnloadKey_function_009AF2FC.md) at `0x009AF489`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00461199` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`.text` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00461190  48 83 EC 28                     sub rsp, 0x28
00461194  B9 01 01 00 00                  mov ecx, 0x101
00461199  E8 52 0F 72 00                  call 0x140b820f0
0046119E  48 83 C4 28                     add rsp, 0x28
004611A2  C3                              ret
004611A3  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpAllocateTransientPoolWithQuota(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = ExAllocatePool2(257, a2, a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void CmpAllocateTransientPoolWithQuota(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = ExAllocatePool2(257, a2, a3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00461190&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00461190[BB_00461190]
  bb_004611A3[BB_004611A3]
```
