# VfIsVerificationEnabledForImage

- RVA: `0x006121D0`–`0x006121F6` (길이 `38` bytes)
- VA: `0x00000001406121D0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `13`개 명령, `38/38` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x006121D9` → [VfDriverLock](../../pagevrfy/B9/VfDriverLock_function_00B9A4A4.md) (function, `0x00B9A4A4`)
- `0x006121E1` → [ViIsDriverSuspectForVerifier](../../pagevrfy/B9/ViIsDriverSuspectForVerifier_function_00B9381C.md) (function, `0x00B9381C`)
- `0x006121E8` → [VfDriverUnlock](../../pagevrfy/B9/VfDriverUnlock_function_00B9A62C.md) (function, `0x00B9A62C`)

### Direct callers
- [KsepPatchDriverImportsTable](../../page/74/KsepPatchDriverImportsTable_function_00749F64.md) at `0x0074A05E`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x006121D9` → [VfDriverLock](../../pagevrfy/B9/VfDriverLock_function_00B9A4A4.md) (`.text` → `PAGEVRFY`)
  - `0x006121E1` → [ViIsDriverSuspectForVerifier](../../pagevrfy/B9/ViIsDriverSuspectForVerifier_function_00B9381C.md) (`.text` → `PAGEVRFY`)
  - `0x006121E8` → [VfDriverUnlock](../../pagevrfy/B9/VfDriverUnlock_function_00B9A62C.md) (`.text` → `PAGEVRFY`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006121D0  40 53                           push rbx
006121D2  48 83 EC 20                     sub rsp, 0x20
006121D6  48 8B D9                        mov rbx, rcx
006121D9  E8 C6 82 58 00                  call 0x140b9a4a4
006121DE  48 8B CB                        mov rcx, rbx
006121E1  E8 36 16 58 00                  call 0x140b9381c
006121E6  8B D8                           mov ebx, eax
006121E8  E8 3F 84 58 00                  call 0x140b9a62c
006121ED  8B C3                           mov eax, ebx
006121EF  48 83 C4 20                     add rsp, 0x20
006121F3  5B                              pop rbx
006121F4  C3                              ret
006121F5  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall VfIsVerificationEnabledForImage(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    result = VfDriverLock(a1, a2, a3, a4);
    result = ViIsDriverSuspectForVerifier(a1, a2, a3, a4);
    result = VfDriverUnlock(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (32);
    return (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))));
}
```

## 5. (Beta) C Style

```c
int64_t VfIsVerificationEnabledForImage(int64_t Arg1)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    result = VfDriverLock(Arg1, a2, a3, a4);
    result = ViIsDriverSuspectForVerifier(Arg1, a2, a3, a4);
    result = VfDriverUnlock(Arg1, a2, a3, a4);
    local_rsp = (local_rsp) + (32);
    return (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))));
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006121D0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006121D0[BB_006121D0]
  bb_006121F5[BB_006121F5]
```
