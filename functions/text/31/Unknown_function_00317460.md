# sub_00317460

- RVA: `0x00317460`–`0x00317476` (길이 `22` bytes)
- VA: `0x0000000140317460`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00074A3C`
- 디코드: `6`개 명령, `22/22` bytes 표시
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
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00317460  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
00317464  45 33 C0                        xor r8d, r8d
00317467  48 89 78 D8                     mov qword ptr [rax - 0x28], rdi
0031746B  4C 8B FA                        mov r15, rdx
0031746E  4C 89 60 D0                     mov qword ptr [rax - 0x30], r12
00317472  48 8D 55 DF                     lea rdx, [rbp - 0x21]
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall sub_00317460(__int64 a1, __int64 a2, int a3)
{
    *(unsigned __int64 *)(result + 16) = v_rbx;
    a3 = 0;
    *(unsigned __int64 *)(result - 40) = v_rdi;
    *(unsigned __int64 *)(result - 48) = v_r12;
    return;
}
```

## 5. (Beta) C Style

```c
void sub_00317460(int64_t Arg1, int64_t Arg2, int32_t Arg3)
{
    *(uint64_t *)(result + 0x10) = local_rbx;
    Arg3 = 0;
    *(uint64_t *)(result - 0x28) = local_rdi;
    *(uint64_t *)(result - 0x30) = local_r12;
    return;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00317460&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00317460[BB_00317460]
```
