# sub_006FCC08

- RVA: `0x006FCC08`–`0x006FCC20` (길이 `24` bytes)
- VA: `0x00000001406FCC08`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BC7A4`
- 디코드: `5`개 명령, `24/24` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x006FCC1B` → [PpmHeteroHgsGetContainmentType + 0x50](../4C/PpmHeteroHgsGetContainmentType_function_004C0AE0.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006FCC08  41 89 1E                        mov dword ptr [r14], ebx
006FCC0B  C6 87 28 03 00 00 01            mov byte ptr [rdi + 0x328], 1
006FCC12  41 8B 06                        mov eax, dword ptr [r14]
006FCC15  89 87 2C 03 00 00               mov dword ptr [rdi + 0x32c], eax
006FCC1B  E9 10 3F DC FF                  jmp 0x1404c0b30
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_006FCC08(void)
{
    *(unsigned int *)(v_r14) = (unsigned int)(v_rbx);
    *(unsigned __int8 *)(v_rdi + 808) = 1;
    *(unsigned int *)(v_rdi + 812) = (unsigned int)((unsigned int)(*(unsigned int *)(v_r14)));
}
```

## 5. (Beta) C Style

```c
void sub_006FCC08(void)
{
    *(uint32_t *)(local_r14) = (uint32_t)(local_rbx);
    *(uint8_t *)(local_rdi + 0x328) = 1;
    *(uint32_t *)(local_rdi + 0x32C) = (uint32_t)((uint32_t)(*(uint32_t *)(local_r14)));
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006FCC08&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006FCC08[BB_006FCC08]
```
