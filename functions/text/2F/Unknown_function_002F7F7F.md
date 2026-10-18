# sub_002F7F7F

- RVA: `0x002F7F7F`–`0x002F7FAE` (길이 `47` bytes)
- VA: `0x00000001402F7F7F`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000724DC`
- 디코드: `10`개 명령, `47/47` bytes 표시
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
  - `0x002F7F9B` → [sub_002F7D3D + 0x9E](Unknown_function_002F7D3D.md) (`tail-transfer`)
  - `0x002F7FA9` → [sub_002F7D3D + 0x8F](Unknown_function_002F7D3D.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
002F7F7F  C7 06 05 00 00 00               mov dword ptr [rsi], 5
002F7F85  48 B8 00 00 00 00 00 80 FF FF   movabs rax, 0xffff800000000000
002F7F8F  48 C7 07 FF FF FF FF            mov qword ptr [rdi], 0xffffffffffffffff
002F7F96  49 89 06                        mov qword ptr [r14], rax
002F7F99  B0 01                           mov al, 1
002F7F9B  E9 3B FE FF FF                  jmp 0x1402f7ddb
002F7FA0  48 89 17                        mov qword ptr [rdi], rdx
002F7FA3  49 8B C0                        mov rax, r8
002F7FA6  4D 89 06                        mov qword ptr [r14], r8
002F7FA9  E9 1E FE FF FF                  jmp 0x1402f7dcc
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_002F7F7F(__int64 a1, __int64 a2, __int64 a3)
{
    *(unsigned int *)(v_rsi) = 5;
    *(unsigned __int64 *)(v_rdi) = -1;
    *(unsigned __int64 *)(v_r14) = result;
}
```

## 5. (Beta) C Style

```c
int64_t sub_002F7F7F(int64_t Arg1, int64_t Arg2, int64_t Arg3)
{
    *(uint32_t *)(local_rsi) = 5;
    *(uint64_t *)(local_rdi) = -1;
    *(uint64_t *)(local_r14) = result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002F7F7F&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002F7F7F[BB_002F7F7F]
  bb_002F7FA0[BB_002F7FA0]
```
