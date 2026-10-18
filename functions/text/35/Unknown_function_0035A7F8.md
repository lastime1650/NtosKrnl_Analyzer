# sub_0035A7F8

- RVA: `0x0035A7F8`–`0x0035A818` (길이 `32` bytes)
- VA: `0x000000014035A7F8`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000799B4`
- 디코드: `7`개 명령, `32/32` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0035A80E` → [KiAcquireQueuedSpinLockInstrumented](../27/KiAcquireQueuedSpinLockInstrumented_function_00275850.md) (function, `0x00275850`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0035A7F8` → RVA `0x00F0DE58` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x0035A800` → [sub_0035A582 + 0x1D3](Unknown_function_0035A582.md) (`tail-transfer`)
  - `0x0035A813` → [sub_0035A582 + 0x1E4](Unknown_function_0035A582.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0035A7F8  8B 05 5A 36 BB 00               mov eax, dword ptr [rip + 0xbb365a]
0035A7FE  85 C0                           test eax, eax
0035A800  0F 85 4F FF FF FF               jne 0x14035a755
0035A806  48 8B D7                        mov rdx, rdi
0035A809  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0035A80E  E8 3D B0 F1 FF                  call 0x140275850
0035A813  E9 4E FF FF FF                  jmp 0x14035a766
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_0035A7F8(void)
{
    __int64 result;
    unsigned __int64 v_stack_p20;

    result = KiAcquireQueuedSpinLockInstrumented(v_stack_p20, v_rdi, a3, a4);
}
```

## 5. (Beta) C Style

```c
void sub_0035A7F8(void)
{
    int64_t result;
    uint64_t v_stack_p20;

    result = KiAcquireQueuedSpinLockInstrumented(v_stack_p20, local_rdi, a3, a4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0035A7F8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0035A7F8[BB_0035A7F8]
  bb_0035A806[BB_0035A806]
  bb_0035A7F8 -->|fallthrough| bb_0035A806
```
