# sub_00241B9E

- RVA: `0x00241B9E`–`0x00241BC7` (길이 `41` bytes)
- VA: `0x0000000140241B9E`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006190C`
- 디코드: `8`개 명령, `41/41` bytes 표시
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
- call이 아닌 외부 분기/꼬리 이동: **3**
  - `0x00241BA1` → [sub_00241A6E + 0x41](Unknown_function_00241A6E.md) (`tail-transfer`)
  - `0x00241BB1` → [sub_006D7C3A](../6D/Unknown_function_006D7C3A.md) (`tail-transfer`)
  - `0x00241BC2` → [sub_006D7C3A](../6D/Unknown_function_006D7C3A.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00241B9E  83 FE 02                        cmp esi, 2
00241BA1  0F 84 08 FF FF FF               je 0x140241aaf
00241BA7  48 8B 8F D0 00 00 00            mov rcx, qword ptr [rdi + 0xd0]
00241BAE  48 85 C9                        test rcx, rcx
00241BB1  0F 85 83 60 49 00               jne 0x1406d7c3a
00241BB7  48 8B 4F 58                     mov rcx, qword ptr [rdi + 0x58]
00241BBB  48 89 8F D0 00 00 00            mov qword ptr [rdi + 0xd0], rcx
00241BC2  E9 73 60 49 00                  jmp 0x1406d7c3a
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall sub_00241B9E(void)
{
    *(unsigned __int64 *)(v_rdi + 208) = *(unsigned __int64 *)(v_rdi + 88);
}
```

## 5. (Beta) C Style

```c
void sub_00241B9E(void)
{
    *(uint64_t *)(local_rdi + 0xD0) = *(uint64_t *)(local_rdi + 0x58);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00241B9E&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00241B9E[BB_00241B9E]
  bb_00241BA7[BB_00241BA7]
  bb_00241BB7[BB_00241BB7]
  bb_00241B9E -->|fallthrough| bb_00241BA7
  bb_00241BA7 -->|fallthrough| bb_00241BB7
```
