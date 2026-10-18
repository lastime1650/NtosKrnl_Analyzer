# sub_006E206A

- RVA: `0x006E206A`–`0x006E2095` (길이 `43` bytes)
- VA: `0x00000001406E206A`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000774E4`
- 디코드: `11`개 명령, `43/43` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x006E206F` → [KeAcquireQueuedSpinLock](../27/KeAcquireQueuedSpinLock_function_00273D80.md) (function, `0x00273D80`)
- `0x006E207D` → [CcInsertVacbArray](../49/CcInsertVacbArray_function_00495768.md) (function, `0x00495768`)
- `0x006E208A` → [KeReleaseQueuedSpinLock](../27/KeReleaseQueuedSpinLock_function_00272540.md) (function, `0x00272540`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x006E2090` → [CcGetVirtualAddress + 0xB7](../34/CcGetVirtualAddress_function_00340C9C.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006E206A  B9 04 00 00 00                  mov ecx, 4
006E206F  E8 0C 1D B9 FF                  call 0x140273d80
006E2074  49 8B D6                        mov rdx, r14
006E2077  49 8B CC                        mov rcx, r12
006E207A  40 8A F8                        mov dil, al
006E207D  E8 E6 36 DB FF                  call 0x140495768
006E2082  40 8A D7                        mov dl, dil
006E2085  B9 04 00 00 00                  mov ecx, 4
006E208A  E8 B1 04 B9 FF                  call 0x140272540
006E208F  90                              nop
006E2090  E9 BE EC C5 FF                  jmp 0x140340d53
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_006E206A(void)
{
    __int64 result;

    result = KeAcquireQueuedSpinLock(4, a2, a3, a4);
    result = CcInsertVacbArray(v_r12, v_r14, a3, a4);
    result = KeReleaseQueuedSpinLock(4, (unsigned __int8)((unsigned __int8)(result)), a3, a4);
}
```

## 5. (Beta) C Style

```c
void sub_006E206A(void)
{
    int64_t result;

    result = KeAcquireQueuedSpinLock(4, a2, a3, a4);
    result = CcInsertVacbArray(local_r12, local_r14, a3, a4);
    result = KeReleaseQueuedSpinLock(4, (uint8_t)((uint8_t)(result)), a3, a4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006E206A&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006E206A[BB_006E206A]
```
