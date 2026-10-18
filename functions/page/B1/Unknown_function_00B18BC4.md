# sub_00B18BC4

- RVA: `0x00B18BC4`–`0x00B18BDE` (길이 `26` bytes)
- VA: `0x0000000140B18BC4`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007C2E4`
- 디코드: `6`개 명령, `26/26` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00B18BC8` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00B18BC8` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x00B18BD3` → [MiLockVadRange + 0x29C](../87/MiLockVadRange_function_0087F670.md) (`tail-transfer`)
  - `0x00B18BD9` → [MiLockVadRange + 0x258](../87/MiLockVadRange_function_0087F670.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00B18BC4  48 8D 4E 28                     lea rcx, [rsi + 0x28]
00B18BC8  E8 33 8A 7C FF                  call 0x1402e1600
00B18BCD  48 8B F7                        mov rsi, rdi
00B18BD0  48 3B FB                        cmp rdi, rbx
00B18BD3  0F 85 33 6D D6 FF               jne 0x14087f90c
00B18BD9  E9 EA 6C D6 FF                  jmp 0x14087f8c8
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00B18BC4(void)
{
    __int64 result;

    result = KeAbPostRelease(v_rsi + 40, a2, a3, a4);
}
```

## 5. (Beta) C Style

```c
void sub_00B18BC4(void)
{
    int64_t result;

    result = KeAbPostRelease(local_rsi + 40, a2, a3, a4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00B18BC4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B18BC4[BB_00B18BC4]
  bb_00B18BD9[BB_00B18BD9]
  bb_00B18BC4 -->|fallthrough| bb_00B18BD9
```
