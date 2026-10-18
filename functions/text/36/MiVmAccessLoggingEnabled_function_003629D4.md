# MiVmAccessLoggingEnabled

- RVA: `0x003629D4`–`0x00362A03` (길이 `47` bytes)
- VA: `0x00000001403629D4`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `12`개 명령, `47/47` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **11**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [MiCombineWithExisting](../22/MiCombineWithExisting_function_0022B4B8.md) at `0x0022B686`
- [MiDecommitAddToList](../24/MiDecommitAddToList_function_00242264.md) at `0x002426B0`
- [MiTrimWorkingSet](../2A/MiTrimWorkingSet_function_002AD134.md) at `0x002AD200`
- [MiTrimSharedPageFromViews](../2E/MiTrimSharedPageFromViews_function_002E16F8.md) at `0x002E1FB2`
- [MiCrcStillIntact](../31/MiCrcStillIntact_function_00317028.md) at `0x00317212`
- [MiCopyOnWrite](MiCopyOnWrite_function_00362A0C.md) at `0x00362F0D`
- [MiDeprioritizeVirtualAddresses](../42/MiDeprioritizeVirtualAddresses_function_0042AD1C.md) at `0x0042AD53`
- [MiCaptureAndResetWorkingSetAccessBits](../47/MiCaptureAndResetWorkingSetAccessBits_function_00473FC0.md) at `0x00474064`
- [NtUnlockVirtualMemory](../4E/NtUnlockVirtualMemory_function_004EE890.md) at `0x004EE941`
- [sub_006D9212](../6D/Unknown_function_006D9212.md) at `0x006D93CF`
- [sub_006DB77C](../6D/Unknown_function_006DB77C.md) at `0x006DB836`

### Static image references
- `0x003629E7` → RVA `0x00E30088` (`.data`; read)
- `0x003629FA` → RVA `0x00E38D00` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003629D4  8B 81 B8 00 00 00               mov eax, dword ptr [rcx + 0xb8]
003629DA  24 0F                           and al, 0xf
003629DC  3C 01                           cmp al, 1
003629DE  74 1A                           je 0x1403629fa
003629E0  0F B7 89 AE 00 00 00            movzx ecx, word ptr [rcx + 0xae]
003629E7  48 8B 05 9A D6 AC 00            mov rax, qword ptr [rip + 0xacd69a]
003629EE  48 8B 04 C8                     mov rax, qword ptr [rax + rcx*8]
003629F2  8B 80 2C 44 00 00               mov eax, dword ptr [rax + 0x442c]
003629F8  C3                              ret
003629F9  CC                              int3
003629FA  48 8D 05 FF 62 AD 00            lea rax, [rip + 0xad62ff]
00362A01  EB EF                           jmp 0x1403629f2
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiVmAccessLoggingEnabled(__int64 a1)
{
    __int64 result;

    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(a1 + 184))) & (15));
    if (((unsigned __int8)(result)) == 1) goto loc_003629FA;
loc_003629F2:
    return (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11327130) + *(unsigned __int16 *)(a1 + 174) * 8) + 17452));
loc_003629FA:
    goto loc_003629F2;
}
```

## 5. (Beta) C Style

```c
int64_t MiVmAccessLoggingEnabled(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;

    result = (uint8_t)(((uint32_t)(*(uint32_t *)(arg1 + 0xB8))) & (15));
    if (((uint8_t)(result)) == 1) goto loc_003629FA;
loc_003629F2:
    return (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xACD69A) + *(uint16_t *)(arg1 + 0xAE) * 8) + 0x442C));
loc_003629FA:
    goto loc_003629F2;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0xAE` | `16` | `R` |
| `Arg1` | `+ 0xB8` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003629D4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003629D4[BB_003629D4]
  bb_003629E0[BB_003629E0]
  bb_003629F2[BB_003629F2]
  bb_003629F9[BB_003629F9]
  bb_003629FA[BB_003629FA]
  bb_003629D4 -->|branch| bb_003629FA
  bb_003629D4 -->|fallthrough| bb_003629E0
  bb_003629E0 -->|flow| bb_003629F2
  bb_003629F9 -->|flow| bb_003629FA
  bb_003629FA -->|branch| bb_003629F2
```
