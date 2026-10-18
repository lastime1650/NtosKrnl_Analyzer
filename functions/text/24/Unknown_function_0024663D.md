# sub_0024663D

- RVA: `0x0024663D`–`0x0024669B` (길이 `94` bytes)
- VA: `0x000000014024663D`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00062008`
- 디코드: `23`개 명령, `94/94` bytes 표시
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
- call이 아닌 외부 분기/꼬리 이동: **7**
  - `0x00246640` → [sub_0024680E + 0xC](Unknown_function_0024680E.md) (`tail-transfer`)
  - `0x00246649` → [sub_00246311 + 0x5C](Unknown_function_00246311.md) (`tail-transfer`)
  - `0x00246652` → [sub_00246311 + 0x5C](Unknown_function_00246311.md) (`tail-transfer`)
  - `0x00246658` → [sub_00246856 + 0xA0](Unknown_function_00246856.md) (`tail-transfer`)
  - `0x00246660` → [sub_00246311 + 0x84](Unknown_function_00246311.md) (`tail-transfer`)
  - `0x00246690` → [sub_002465E2 + 0x6](Unknown_function_002465E2.md) (`tail-transfer`)
  - `0x00246696` → [sub_00246311 + 0xAD](Unknown_function_00246311.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0024663D  49 3B D0                        cmp rdx, r8
00246640  0F 83 D4 01 00 00               jae 0x14024681a
00246646  48 3B D1                        cmp rdx, rcx
00246649  0F 82 1E FD FF FF               jb 0x14024636d
0024664F  48 3B C1                        cmp rax, rcx
00246652  0F 83 15 FD FF FF               jae 0x14024636d
00246658  E9 99 02 00 00                  jmp 0x1402468f6
0024665D  83 F8 FF                        cmp eax, -1
00246660  0F 85 2F FD FF FF               jne 0x140246395
00246666  B9 C0 00 00 00                  mov ecx, 0xc0
0024666B  3B D1                           cmp edx, ecx
0024666D  7E 1E                           jle 0x14024668d
0024666F  83 FA FF                        cmp edx, -1
00246672  74 19                           je 0x14024668d
00246674  8B C2                           mov eax, edx
00246676  F0 41 0F B1 88 9C 8B 00 00      lock cmpxchg dword ptr [r8 + 0x8b9c], ecx
0024667F  75 0C                           jne 0x14024668d
00246681  8D 82 40 FF FF FF               lea eax, [rdx - 0xc0]
00246687  4C 63 C8                        movsxd r9, eax
0024668A  49 FF C1                        inc r9
0024668D  4D 85 C9                        test r9, r9
00246690  0F 85 52 FF FF FF               jne 0x1402465e8
00246696  E9 23 FD FF FF                  jmp 0x1402463be
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_0024663D(__int64 a1, __int64 a2, __int64 a3)
{
}
```

## 5. (Beta) C Style

```c
int64_t sub_0024663D(int64_t Arg1, int64_t Arg2, int64_t Arg3)
{
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0024663D&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0024663D[BB_0024663D]
  bb_00246646[BB_00246646]
  bb_0024664F[BB_0024664F]
  bb_00246658[BB_00246658]
  bb_0024665D[BB_0024665D]
  bb_00246666[BB_00246666]
  bb_0024666F[BB_0024666F]
  bb_00246674[BB_00246674]
  bb_00246681[BB_00246681]
  bb_0024668D[BB_0024668D]
  bb_00246696[BB_00246696]
  bb_0024663D -->|fallthrough| bb_00246646
  bb_00246646 -->|fallthrough| bb_0024664F
  bb_0024664F -->|fallthrough| bb_00246658
  bb_0024665D -->|fallthrough| bb_00246666
  bb_00246666 -->|branch| bb_0024668D
  bb_00246666 -->|fallthrough| bb_0024666F
  bb_0024666F -->|branch| bb_0024668D
  bb_0024666F -->|fallthrough| bb_00246674
  bb_00246674 -->|branch| bb_0024668D
  bb_00246674 -->|fallthrough| bb_00246681
  bb_00246681 -->|flow| bb_0024668D
  bb_0024668D -->|fallthrough| bb_00246696
```
