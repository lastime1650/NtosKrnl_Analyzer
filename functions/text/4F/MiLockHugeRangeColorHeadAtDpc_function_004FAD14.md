# MiLockHugeRangeColorHeadAtDpc

- RVA: `0x004FAD14`–`0x004FAD34` (길이 `32` bytes)
- VA: `0x00000001404FAD14`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `11`개 명령, `32/32` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x004FAD1A` → [MiComputeHugeRangeColorHeadAtDpc](../43/MiComputeHugeRangeColorHeadAtDpc_function_00436968.md) (function, `0x00436968`)
- `0x004FAD25` → [MiLockColorHeadHugeAtDpc](MiLockColorHeadHugeAtDpc_function_004FAD3C.md) (function, `0x004FAD3C`)

### Direct callers
- [MiHugeRangeFreeToZero](../43/MiHugeRangeFreeToZero_function_00436A38.md) at `0x00436A6A`
- [MiStopHugePageAccessor](MiStopHugePageAccessor_function_004F6A68.md) at `0x004F6AA7`
- [MiCanBeginHugeIoPageAccessor](../67/MiCanBeginHugeIoPageAccessor_function_00675370.md) at `0x00675393`
- [MiMarkHugePfnBad](../67/MiMarkHugePfnBad_function_00676744.md) at `0x0067690F`
- [MiMarkHugePfnBad](../67/MiMarkHugePfnBad_function_00676744.md) at `0x00676A67`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004FAD14  40 53                           push rbx
004FAD16  48 83 EC 20                     sub rsp, 0x20
004FAD1A  E8 49 BC F3 FF                  call 0x140436968
004FAD1F  48 8B C8                        mov rcx, rax
004FAD22  48 8B D8                        mov rbx, rax
004FAD25  E8 12 00 00 00                  call 0x1404fad3c
004FAD2A  48 8B C3                        mov rax, rbx
004FAD2D  48 83 C4 20                     add rsp, 0x20
004FAD31  5B                              pop rbx
004FAD32  C3                              ret
004FAD33  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiLockHugeRangeColorHeadAtDpc(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    result = MiComputeHugeRangeColorHeadAtDpc(a1, a2, a3, a4);
    result = MiLockColorHeadHugeAtDpc(result, a2, a3, a4);
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
void MiLockHugeRangeColorHeadAtDpc(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    result = MiComputeHugeRangeColorHeadAtDpc(a1, a2, a3, a4);
    result = MiLockColorHeadHugeAtDpc(result, a2, a3, a4);
    local_rsp = (local_rsp) + (32);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004FAD14&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004FAD14[BB_004FAD14]
  bb_004FAD33[BB_004FAD33]
```
