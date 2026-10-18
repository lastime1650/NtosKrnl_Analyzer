# MiEndingOffset

- RVA: `0x002ACEC8`–`0x002ACF0B` (길이 `67` bytes)
- VA: `0x00000001402ACEC8`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `22`개 명령, `67/67` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **6**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [MiInitializeImageProtos](MiInitializeImageProtos_function_002ABDAC.md) at `0x002ABE5B`
- [MiFinishMdlForMappedFileFault](MiFinishMdlForMappedFileFault_function_002AC974.md) at `0x002ACA72`
- [MiCanFileBeTruncatedInternal](MiCanFileBeTruncatedInternal_function_002ACCB4.md) at `0x002ACD99`
- [MiCopyDataPageToImagePage](MiCopyDataPageToImagePage_function_002AE818.md) at `0x002AE94E`
- [MiFlushSection](../40/MiFlushSection_function_004036B0.md) at `0x00403F21`
- [MiFlushSection](../40/MiFlushSection_function_004036B0.md) at `0x004043CE`
- [MiAllocateFileExtents](../../page/AB/MiAllocateFileExtents_function_00ABDF54.md) at `0x00ABDFEC`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
002ACEC8  48 8B 01                        mov rax, qword ptr [rcx]
002ACECB  8B 50 38                        mov edx, dword ptr [rax + 0x38]
002ACECE  F6 C2 20                        test dl, 0x20
002ACED1  75 29                           jne 0x1402acefc
002ACED3  8B 51 20                        mov edx, dword ptr [rcx + 0x20]
002ACED6  8B 41 24                        mov eax, dword ptr [rcx + 0x24]
002ACED9  81 E2 C0 FF 00 00               and edx, 0xffc0
002ACEDF  48 C1 E2 1A                     shl rdx, 0x1a
002ACEE3  48 0B D0                        or rdx, rax
002ACEE6  8B 41 28                        mov eax, dword ptr [rcx + 0x28]
002ACEE9  48 03 D0                        add rdx, rax
002ACEEC  48 C1 E2 0C                     shl rdx, 0xc
002ACEF0  8B 41 20                        mov eax, dword ptr [rcx + 0x20]
002ACEF3  48 C1 E8 14                     shr rax, 0x14
002ACEF7  48 03 C2                        add rax, rdx
002ACEFA  C3                              ret
002ACEFB  CC                              int3
002ACEFC  8B 51 28                        mov edx, dword ptr [rcx + 0x28]
002ACEFF  8B 41 24                        mov eax, dword ptr [rcx + 0x24]
002ACF02  48 03 D0                        add rdx, rax
002ACF05  48 C1 E2 09                     shl rdx, 9
002ACF09  EB E5                           jmp 0x1402acef0
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiEndingOffset(__int64 a1)
{
    __int64 result;

    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 56)))) & (32)) != 0) goto loc_002ACEFC;
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 32))) & (0xFFC0ULL));
    a2 = (a2) << (26);
    a2 = (a2) | ((unsigned int)(*(unsigned int *)(a1 + 36)));
    a2 = (a2) + ((unsigned int)(*(unsigned int *)(a1 + 40)));
    a2 = (a2) << (12);
loc_002ACEF0:
    result = ((unsigned int)(*(unsigned int *)(a1 + 32))) >> (20);
    result = (result) + (a2);
    return result;
loc_002ACEFC:
    a2 = ((unsigned int)(*(unsigned int *)(a1 + 40))) + ((unsigned int)(*(unsigned int *)(a1 + 36)));
    a2 = (a2) << (9);
    goto loc_002ACEF0;
}
```

## 5. (Beta) C Style

```c
int64_t MiEndingOffset(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;

    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0x38)))) & (32)) != 0) goto loc_002ACEFC;
    a2 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x20))) & (0xFFC0ULL));
    a2 = (a2) << (26);
    a2 = (a2) | ((uint32_t)(*(uint32_t *)(arg1 + 0x24)));
    a2 = (a2) + ((uint32_t)(*(uint32_t *)(arg1 + 0x28)));
    a2 = (a2) << (12);
loc_002ACEF0:
    result = ((uint32_t)(*(uint32_t *)(arg1 + 0x20))) >> (20);
    result = (result) + (a2);
    return result;
loc_002ACEFC:
    a2 = ((uint32_t)(*(uint32_t *)(arg1 + 0x28))) + ((uint32_t)(*(uint32_t *)(arg1 + 0x24)));
    a2 = (a2) << (9);
    goto loc_002ACEF0;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x20` | `32` | `R` |
| `Arg1` | `+ 0x24` | `32` | `R` |
| `Arg1` | `+ 0x28` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002ACEC8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002ACEC8[BB_002ACEC8]
  bb_002ACED3[BB_002ACED3]
  bb_002ACEF0[BB_002ACEF0]
  bb_002ACEFB[BB_002ACEFB]
  bb_002ACEFC[BB_002ACEFC]
  bb_002ACEC8 -->|branch| bb_002ACEFC
  bb_002ACEC8 -->|fallthrough| bb_002ACED3
  bb_002ACED3 -->|flow| bb_002ACEF0
  bb_002ACEFB -->|flow| bb_002ACEFC
  bb_002ACEFC -->|branch| bb_002ACEF0
```
