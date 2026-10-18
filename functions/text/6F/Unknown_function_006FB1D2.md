# sub_006FB1D2

- RVA: `0x006FB1D2`–`0x006FB213` (길이 `65` bytes)
- VA: `0x00000001406FB1D2`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000B88F8`
- 디코드: `17`개 명령, `65/65` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x006FB1E0` → [IopMaskInterrupt](../2D/IopMaskInterrupt_function_002D3D2C.md) (function, `0x002D3D2C`)
- `0x006FB1FF` → [IopMaskInterrupt](../2D/IopMaskInterrupt_function_002D3D2C.md) (function, `0x002D3D2C`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x006FB1EC` → [IoReportInterruptInactive + 0x2B](../4B/IoReportInterruptInactive_function_004B02E0.md) (`tail-transfer`)
  - `0x006FB20E` → [IoReportInterruptInactive + 0x2B](../4B/IoReportInterruptInactive_function_004B02E0.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006FB1D2  8B C3                           mov eax, ebx
006FB1D4  48 8D 0C 40                     lea rcx, [rax + rax*2]
006FB1D8  48 03 C9                        add rcx, rcx
006FB1DB  48 8B 4C CF 18                  mov rcx, qword ptr [rdi + rcx*8 + 0x18]
006FB1E0  E8 47 8B BD FF                  call 0x1402d3d2c
006FB1E5  FF C3                           inc ebx
006FB1E7  3B 5F 04                        cmp ebx, dword ptr [rdi + 4]
006FB1EA  72 E6                           jb 0x1406fb1d2
006FB1EC  E9 1A 51 DB FF                  jmp 0x1404b030b
006FB1F1  8B C3                           mov eax, ebx
006FB1F3  48 8B 8C C7 28 01 00 00         mov rcx, qword ptr [rdi + rax*8 + 0x128]
006FB1FB  48 83 C1 70                     add rcx, 0x70
006FB1FF  E8 28 8B BD FF                  call 0x1402d3d2c
006FB204  FF C3                           inc ebx
006FB206  3B 9F 24 01 00 00               cmp ebx, dword ptr [rdi + 0x124]
006FB20C  72 E3                           jb 0x1406fb1f1
006FB20E  E9 F8 50 DB FF                  jmp 0x1404b030b
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_006FB1D2(void)
{
    __int64 result;
    __int64 v_rbx;

    a1 = ((unsigned int)((unsigned int)(v_rbx)) + (unsigned int)((unsigned int)(v_rbx)) * 2) + ((unsigned int)((unsigned int)(v_rbx)) + (unsigned int)((unsigned int)(v_rbx)) * 2);
    result = IopMaskInterrupt(*(unsigned __int64 *)(v_rdi + a1 * 8 + 24), a2, a3, a4);
    v_rbx = (unsigned int)((v_rbx) + 1);
    if (((unsigned int)(v_rbx)) < (*(unsigned int *)(v_rdi + 4))) goto loc_006FB1D2;
}
```

## 5. (Beta) C Style

```c
void sub_006FB1D2(void)
{
    int64_t result;
    int64_t local_rbx;

    a1 = ((uint32_t)((uint32_t)(local_rbx)) + (uint32_t)((uint32_t)(local_rbx)) * 2) + ((uint32_t)((uint32_t)(local_rbx)) + (uint32_t)((uint32_t)(local_rbx)) * 2);
    result = IopMaskInterrupt(*(uint64_t *)(local_rdi + a1 * 8 + 0x18), a2, a3, a4);
    local_rbx = (uint32_t)((local_rbx) + 1);
    if (((uint32_t)(local_rbx)) < (*(uint32_t *)(local_rdi + 0x4))) goto loc_006FB1D2;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006FB1D2&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006FB1D2[BB_006FB1D2]
  bb_006FB1EC[BB_006FB1EC]
  bb_006FB1F1[BB_006FB1F1]
  bb_006FB20E[BB_006FB20E]
  bb_006FB1D2 -->|branch| bb_006FB1D2
  bb_006FB1D2 -->|fallthrough| bb_006FB1EC
  bb_006FB1F1 -->|branch| bb_006FB1F1
  bb_006FB1F1 -->|fallthrough| bb_006FB20E
```
