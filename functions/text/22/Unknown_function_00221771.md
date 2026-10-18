# sub_00221771

- RVA: `0x00221771`–`0x0022178C` (길이 `27` bytes)
- VA: `0x0000000140221771`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005F584`
- 디코드: `6`개 명령, `27/27` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00221782` → [KiAcquireQueuedSpinLockInstrumented](../27/KiAcquireQueuedSpinLockInstrumented_function_00275850.md) (function, `0x00275850`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00221771` → RVA `0x00F0DE58` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x00221779` → [KiAbEntryGetLockedHeadEntry + 0x45](KiAbEntryGetLockedHeadEntry_function_002213C0.md) (`tail-transfer`)
  - `0x00221787` → [KiAbEntryGetLockedHeadEntry + 0x54](KiAbEntryGetLockedHeadEntry_function_002213C0.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00221771  8B 05 E1 C6 CE 00               mov eax, dword ptr [rip + 0xcec6e1]
00221777  85 C0                           test eax, eax
00221779  0F 85 86 FC FF FF               jne 0x140221405
0022177F  49 8B CE                        mov rcx, r14
00221782  E8 C9 40 05 00                  call 0x140275850
00221787  E9 88 FC FF FF                  jmp 0x140221414
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00221771(void)
{
    __int64 result;

    result = KiAcquireQueuedSpinLockInstrumented(v_r14, a2, a3, a4);
}
```

## 5. (Beta) C Style

```c
void sub_00221771(void)
{
    int64_t result;

    result = KiAcquireQueuedSpinLockInstrumented(local_r14, a2, a3, a4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00221771&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00221771[BB_00221771]
  bb_0022177F[BB_0022177F]
  bb_00221771 -->|fallthrough| bb_0022177F
```
