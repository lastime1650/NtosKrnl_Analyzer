# sub_00415276

- RVA: `0x00415276`–`0x00415292` (길이 `28` bytes)
- VA: `0x0000000140415276`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0009C268`
- 디코드: `7`개 명령, `28/28` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0041528B` → [FsRtlpWaitForIoAtEof](FsRtlpWaitForIoAtEof_function_00415298.md) (function, `0x00415298`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x0041527A` → [sub_00415212 + 0x1C](Unknown_function_00415212.md) (`tail-transfer`)
  - `0x00415290` → [sub_00415212 + 0x1C](Unknown_function_00415212.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00415276  66 FF 47 26                     inc word ptr [rdi + 0x26]
0041527A  EB B2                           jmp 0x14041522e
0041527C  48 8B 54 24 78                  mov rdx, qword ptr [rsp + 0x78]
00415281  49 C7 C0 FF FF FF FF            mov r8, 0xffffffffffffffff
00415288  48 8B CF                        mov rcx, rdi
0041528B  E8 08 00 00 00                  call 0x140415298
00415290  EB 9C                           jmp 0x14041522e
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00415276(void)
{
    unsigned __int64 v_stack_p78;
}
```

## 5. (Beta) C Style

```c
void sub_00415276(void)
{
    uint64_t v_stack_p78;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00415276&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00415276[BB_00415276]
  bb_0041527C[BB_0041527C]
```
