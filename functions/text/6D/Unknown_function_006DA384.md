# sub_006DA384

- RVA: `0x006DA384`–`0x006DA3C8` (길이 `68` bytes)
- VA: `0x00000001406DA384`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00066E88`
- 디코드: `16`개 명령, `68/68` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x006DA38A` → [MiUnlockPage](../31/MiUnlockPage_function_0031A3E0.md) (function, `0x0031A3E0`)
- `0x006DA3AC` → [MiUnlockPage](../31/MiUnlockPage_function_0031A3E0.md) (function, `0x0031A3E0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **4**
  - `0x006DA394` → [MiGetPerfectColorHeadPage + 0x8A](../28/MiGetPerfectColorHeadPage_function_00289CA8.md) (`tail-transfer`)
  - `0x006DA3A1` → [MiGetPerfectColorHeadPage + 0x8A](../28/MiGetPerfectColorHeadPage_function_00289CA8.md) (`tail-transfer`)
  - `0x006DA3B6` → [MiGetPerfectColorHeadPage + 0x240](../28/MiGetPerfectColorHeadPage_function_00289CA8.md) (`tail-transfer`)
  - `0x006DA3C3` → [MiGetPerfectColorHeadPage + 0x297](../28/MiGetPerfectColorHeadPage_function_00289CA8.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006DA384  40 8A D6                        mov dl, sil
006DA387  48 8B CF                        mov rcx, rdi
006DA38A  E8 51 00 C4 FF                  call 0x14031a3e0
006DA38F  4C 8B 74 24 28                  mov r14, qword ptr [rsp + 0x28]
006DA394  E9 99 F9 BA FF                  jmp 0x140289d32
006DA399  40 0F B6 C6                     movzx eax, sil
006DA39D  44 0F 22 C0                     mov cr8, rax
006DA3A1  E9 8C F9 BA FF                  jmp 0x140289d32
006DA3A6  40 8A D6                        mov dl, sil
006DA3A9  48 8B CF                        mov rcx, rdi
006DA3AC  E8 2F 00 C4 FF                  call 0x14031a3e0
006DA3B1  B8 02 00 00 00                  mov eax, 2
006DA3B6  E9 2D FB BA FF                  jmp 0x140289ee8
006DA3BB  40 0F B6 C6                     movzx eax, sil
006DA3BF  44 0F 22 C0                     mov cr8, rax
006DA3C3  E9 77 FB BA FF                  jmp 0x140289f3f
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_006DA384(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5)
{
    __int64 result;

    result = MiUnlockPage(v_rdi, (unsigned __int8)(v_rsi), a3, a4);
}
```

## 5. (Beta) C Style

```c
int64_t sub_006DA384(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, int64_t Arg5)
{
    int64_t result;

    result = MiUnlockPage(local_rdi, (uint8_t)(local_rsi), Arg3, Arg4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006DA384&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006DA384[BB_006DA384]
  bb_006DA399[BB_006DA399]
  bb_006DA3A6[BB_006DA3A6]
  bb_006DA3BB[BB_006DA3BB]
```
