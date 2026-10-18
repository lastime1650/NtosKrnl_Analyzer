# sub_00401CA4

- RVA: `0x00401CA4`–`0x00401CBE` (길이 `26` bytes)
- VA: `0x0000000140401CA4`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0009A5E0`
- 디코드: `6`개 명령, `26/26` bytes 표시
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
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x00401CAE` → [ExIsFastResourceHeld + 0x9C](ExIsFastResourceHeld_function_00401AE0.md) (`tail-transfer`)
  - `0x00401CB9` → [ExIsFastResourceHeld + 0xB8](ExIsFastResourceHeld_function_00401AE0.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00401CA4  48 8B 09                        mov rcx, qword ptr [rcx]
00401CA7  49 FF C0                        inc r8
00401CAA  49 83 F8 06                     cmp r8, 6
00401CAE  0F 86 C8 FE FF FF               jbe 0x140401b7c
00401CB4  BB 01 00 00 00                  mov ebx, 1
00401CB9  E9 DA FE FF FF                  jmp 0x140401b98
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall sub_00401CA4(__int64 a1, __int64 a2, __int64 a3)
{
    a3 = (a3) + 1;
}
```

## 5. (Beta) C Style

```c
void sub_00401CA4(void *Arg1, int64_t Arg2, int64_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    Arg3 = (Arg3) + 1;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00401CA4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00401CA4[BB_00401CA4]
  bb_00401CB4[BB_00401CB4]
  bb_00401CA4 -->|fallthrough| bb_00401CB4
```
