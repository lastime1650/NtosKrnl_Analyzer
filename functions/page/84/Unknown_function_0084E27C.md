# sub_0084E27C

- RVA: `0x0084E27C`–`0x0084E299` (길이 `29` bytes)
- VA: `0x000000014084E27C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00069BE0`
- 디코드: `9`개 명령, `29/29` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0084E283` → [CmEqualTrans](CmEqualTrans_function_0084BF60.md) (function, `0x0084BF60`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **3**
  - `0x0084E28A` → [sub_0084E244 + 0x11](Unknown_function_0084E244.md) (`tail-transfer`)
  - `0x0084E291` → [sub_0084E244 + 0x11](Unknown_function_0084E244.md) (`tail-transfer`)
  - `0x0084E297` → [sub_0084E244 + 0x2C](Unknown_function_0084E244.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0084E27C  49 8B 4E 38                     mov rcx, qword ptr [r14 + 0x38]
0084E280  48 8B D7                        mov rdx, rdi
0084E283  E8 D8 DC FF FF                  call 0x14084bf60
0084E288  84 C0                           test al, al
0084E28A  74 C9                           je 0x14084e255
0084E28C  41 83 7E 44 08                  cmp dword ptr [r14 + 0x44], 8
0084E291  75 C2                           jne 0x14084e255
0084E293  49 8B 5E 58                     mov rbx, qword ptr [r14 + 0x58]
0084E297  EB D7                           jmp 0x14084e270
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_0084E27C(void)
{
    __int64 result;

    result = CmEqualTrans(*(unsigned __int64 *)(v_r14 + 56), v_rdi, a3, a4);
}
```

## 5. (Beta) C Style

```c
void sub_0084E27C(void)
{
    int64_t result;

    result = CmEqualTrans(*(uint64_t *)(local_r14 + 0x38), local_rdi, a3, a4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0084E27C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0084E27C[BB_0084E27C]
  bb_0084E28C[BB_0084E28C]
  bb_0084E293[BB_0084E293]
  bb_0084E27C -->|fallthrough| bb_0084E28C
  bb_0084E28C -->|fallthrough| bb_0084E293
```
