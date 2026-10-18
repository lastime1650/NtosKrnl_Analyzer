# sub_00262F4A

- RVA: `0x00262F4A`–`0x00262F6E` (길이 `36` bytes)
- VA: `0x0000000140262F4A`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00064640`
- 디코드: `9`개 명령, `36/36` bytes 표시
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
- call이 아닌 외부 분기/꼬리 이동: **4**
  - `0x00262F4C` → [sub_00262D5A + 0x32](Unknown_function_00262D5A.md) (`tail-transfer`)
  - `0x00262F55` → [sub_00262D5A + 0x38](Unknown_function_00262D5A.md) (`tail-transfer`)
  - `0x00262F5C` → [sub_00262D5A + 0xC7](Unknown_function_00262D5A.md) (`tail-transfer`)
  - `0x00262F69` → [sub_00262D5A + 0xCD](Unknown_function_00262D5A.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00262F4A  39 2A                           cmp dword ptr [rdx], ebp
00262F4C  0F 87 3A FE FF FF               ja 0x140262d8c
00262F52  44 8B DD                        mov r11d, ebp
00262F55  E9 38 FE FF FF                  jmp 0x140262d92
00262F5A  39 2A                           cmp dword ptr [rdx], ebp
00262F5C  0F 87 BF FE FF FF               ja 0x140262e21
00262F62  48 8B C8                        mov rcx, rax
00262F65  48 83 E1 FD                     and rcx, 0xfffffffffffffffd
00262F69  E9 B9 FE FF FF                  jmp 0x140262e27
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall sub_00262F4A(__int64 a1, __int64 a2)
{
}
```

## 5. (Beta) C Style

```c
void sub_00262F4A(int64_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00262F4A&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00262F4A[BB_00262F4A]
  bb_00262F52[BB_00262F52]
  bb_00262F5A[BB_00262F5A]
  bb_00262F62[BB_00262F62]
  bb_00262F4A -->|fallthrough| bb_00262F52
  bb_00262F5A -->|fallthrough| bb_00262F62
```
