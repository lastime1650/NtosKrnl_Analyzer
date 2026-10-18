# sub_002D958F

- RVA: `0x002D958F`–`0x002D95B2` (길이 `35` bytes)
- VA: `0x00000001402D958F`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007036C`
- 디코드: `7`개 명령, `35/35` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x002D959F` → RVA `0x00FC6D20` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x002D95B0` → [sub_002D95B2 + 0xD](Unknown_function_002D95B2.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
002D958F  4C 8B 6C 24 28                  mov r13, qword ptr [rsp + 0x28]
002D9594  48 8B 6C 24 48                  mov rbp, qword ptr [rsp + 0x48]
002D9599  89 BE 78 88 00 00               mov dword ptr [rsi + 0x8878], edi
002D959F  83 3D 7A D7 CE 00 00            cmp dword ptr [rip + 0xced77a], 0
002D95A6  48 8B 7C 24 38                  mov rdi, qword ptr [rsp + 0x38]
002D95AB  48 8B 74 24 40                  mov rsi, qword ptr [rsp + 0x40]
002D95B0  74 0D                           je 0x1402d95bf
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall sub_002D958F(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9)
{
    *(unsigned int *)(v_rsi + 34936) = (unsigned int)(v_rdi);
}
```

## 5. (Beta) C Style

```c
void sub_002D958F(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, int64_t Arg5, uint64_t Arg6, int64_t Arg7, int64_t Arg8, int64_t Arg9)
{
    *(uint32_t *)(local_rsi + 0x8878) = (uint32_t)(local_rdi);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002D958F&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002D958F[BB_002D958F]
```
